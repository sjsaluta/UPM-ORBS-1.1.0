from distutils.command.build import build
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from UPM.filters import RoomFilter
from . forms import *
from bookingapp.forms import *
from bookingapp.models import *

import pandas as pd
import re
from datetime import datetime
# Create your views here.

def indexPage(request):
    return redirect(dashBoardPage)

def uploadPage(request):
    form = UploadForm()
    ocs = OCS.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(False)
            f.ocs=ocs
            f.college=ocs.college
            f.save()

            ''' The next lines parse the data from csv to Schedule Model'''

            file = ScheduleFile.objects.get(file = f.file.name)
            df = pd.read_csv('media/'+f.file.name).iloc[7:,[0,1,2,4,5,6,7,8,9]]
            df.columns=['Class No.','Course Title','Subject','Section','Component','Schedule','Room','Instructor','Class Capacity']
            df = df[df["Room"].str.contains("TBA") == False]
            cn = df['Class No.'].tolist()
            ct = df['Course Title'].tolist()
            sub = df['Subject'].tolist()
            sec = df["Section"].tolist()
            com = df['Component'].tolist()
            rm = df['Room'].tolist()
            ins = df['Instructor'].tolist()
            cap = df['Class Capacity'].tolist()
            time = df["Schedule"]

            x=re.findall(r'\s(\d{2}\:\d{2}\s?(?:AM|PM|am|pm)\s?\-\s?\d{2}\:\d{2}\s?(?:AM|PM|am|pm))',time.to_string())
            start_time = []
            end_time = []
            for i in x:
                tf = i.split(' - ')
                start_time.append(tf[0])
                end_time.append(tf[1])
                y=re.findall(r"\bM\w*|\bT\w*|\bW\w*|\bS\w*|\bF\w*",time.to_string())

            term = Term.objects.get(slug = '2022-2023')
            for i in range(len(df)):
                r = rm[i]
                r=r.replace(" ","")
                room = Room.objects.get(name=r)
                days= ''
                day = re.findall("M|TH|T|W|F|S",y[i])
                for ds in range(len(day)):
                    if day[ds] == 'M':
                        day[ds]='1'
                    elif day[ds] == 'T':
                        day[ds]='2'
                    elif day[ds] == 'W':
                        day[ds]='3'
                    elif day[ds] == 'TH':
                        day[ds]='4'
                    elif day[ds] == 'F':
                        day[ds]='5'
                    elif day[ds] == 'S':
                        day[ds]='6'
                for d in day:
                    days += d
                st = datetime.strptime(start_time[i],"%I:%M %p").time()
                et = datetime.strptime(end_time[i],"%I:%M %p").time()
                
                Schedule.objects.create(
                    schedfile = file,
                    room=room,
                    faculty=ins[i],
                    coursetitle=ct[i],
                    classnum=cn[i],
                    component=com[i],
                    subject=sub[i],
                    section=sec[i],
                    capacity=cap[i],
                    time_start=st,
                    time_end=et,
                    dayofweek=days
                    )

            ''' endline '''    

    context={'form':form}
    return render(request,'UPM/upload.html',context)

@login_required(login_url='loginPage')
def dashBoardPage(request):
        
    return render(request,"UPM/dashboard.html")

#### Admin Views #####

#manage terms
@login_required(login_url='loginPage')
def manageTerm(request):
    terms = Term.objects.all()
    context={'terms':terms}
    return render(request,"UPM/term.html",context)

@login_required(login_url='loginPage')
def termView(request, slug):
    term = Term.objects.get(slug=slug)
    rooms = term.room.all()
    rms = Room.objects.all()

    #Checks if rooms are already in term
    room_exclude = []
    for rm in rms:
        for room in rooms:
            if room == rm:
                room_exclude.append(rm)
    room_term = Room.objects.exclude(name__in=room_exclude)
    if request.method == "POST":
        room = request.POST.getlist('rooms')
        print(room)
        for rm in room:
            if Room.objects.all().exists():
                rm = Room.objects.get(slug=rm)
                term.room.add(rm)      
        if request.POST.get("activate"):
            term.isActivated=True
            term.save()
        elif request.POST.get("deactivate"):
            term.isActivated=False
            term.save()
        return redirect(reverse('termView',kwargs={'slug':slug}))   
    context ={'term':term,'rooms':rooms,'rms':room_term}
    return render(request,"UPM/term-details.html",context)

@login_required(login_url='loginPage')
def addTerm(request):
    form = AddTerm()
    if request.method == "POST":
        form = AddTerm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-term.html",context)

#manage colleges
@login_required(login_url='loginPage')
def manageCollege(request):
    colleges = College.objects.all()
    context={'colleges':colleges}
    return render(request,"UPM/college.html",context)

@login_required(login_url='loginPage')
def addCollege(request):
    form = AddCollege()
    if request.method == "POST":
        form = AddCollege(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-college.html",context)

@login_required(login_url='loginPage')
def addDept(request,slug):
    college = College.objects.get(slug=slug)
    form = AddDept()
    if request.method == "POST":
        form = AddDept(request.POST)
        if form.is_valid():
            dept = form.save(False)
            dept.college = college
            dept.save()
    context={'form':form}
    return render(request,"UPM/add-dept.html",context)

@login_required(login_url='loginPage')
def addBuild(request,slug):
    college = College.objects.get(slug=slug)
    form = AddBuild()
    if request.method == "POST":
        form = AddBuild(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.college = college
            build.save()

    context={'form':form}
    return render(request,"UPM/add-build.html",context)

@login_required(login_url='loginPage')
def addRoom(request):
    frbuild=False
    form = AddRoom()
    if request.method == "POST":
        form = AddRoom(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form,'frbuild':frbuild}
    return render(request,"UPM/add-room.html",context)

@login_required(login_url='loginPage')
def addBuildRoom(request,c,b):
    frbuild = True
    college = College.objects.get(slug=c)
    building= Building.objects.get(slug=b)
    form = AddRoom()
    if request.method == "POST":
        form = AddRoom(request.POST)
        if form.is_valid():
            room = form.save(False)
            room.college = college
            room.building = building
            room.save()
            return redirect(reverse('adminBuildingView',kwargs={"c": college.slug,"b":building.slug}))
    context={'form':form,'frbuild':frbuild}
    return render(request,"UPM/add-room.html",context)
    
#manage rooms
@login_required(login_url='loginPage')
def manageRooms(request):
    rooms=Room.objects.all()
    form = ColBuildForm()

    if request.method == "POST":
        form = ColBuildForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data.get
            col_selected = College.objects.filter(name=room('college_select'))
            build_selected = Building.objects.filter(name=room('build_select'))
            r = form.save(False)
            r.building = build_selected[0]
            r.college = col_selected[0]
            r.save()

    context={'rooms':rooms,'form':form}
    return render(request,"UPM/room.html",context)

##### User Views #####
@login_required(login_url='loginPage')
def calendarView(request, slug):
    room = Room.objects.get(slug=slug)
    terms = Term.objects.filter(room=room)
    term = None
    for t in terms:
        if t.isActivated:
            term = t
    schedfile = ScheduleFile.objects.get(term=term)
    schedule = Schedule.objects.filter(room=room,schedfile=schedfile)
    form = AddBookFrCal()
    if request.method == "POST":
        form = AddBookFrCal(request.POST)
        if form.is_valid():
            book = form.save(False)
            book.room = room
            if(request.user.user_type == 1):
                book.faculty=request.user
                book.booker=request.user
            else:
                book.booker=request.user
            book.save()

    booking = Booking.objects.filter(room_id=room.id)

    context={'booking':booking,'room':room,'term':term,'form':form,'sched':schedule}
    return render(request,"UPM/calendar.html",context)

@login_required(login_url='loginPage')
def collegeView(request, slug):
    college = College.objects.get(slug= slug)

    if request.method == 'POST':
        if request.POST.get('build'):
            field = college.building_set.all()
            view = 'build'
        else:
            field = college.department_set.all()
            view = 'dept'
        context={'fields':field,'college':college,'view':view}   
    else:
        view = 'dept'
        field = college.department_set.all()    
        context={'fields':field,'college':college,'view':view} 
         
    return render(request,'UPM/college-details.html',context)

@login_required(login_url='loginPage')
def buildingView(request,c,b):
    college = College.objects.get(slug=c)
    building= Building.objects.get(slug=b)
    room = Room.objects.filter(building=building).order_by('name')
    context={'rooms':room,'building':building,'college':college}
    return render(request,'UPM/building-details.html',context)

@login_required(login_url='loginPage')
def roomView(request):
    rooms = Room.objects.all()
    rfilter= RoomFilter(request.GET,queryset=rooms)
    build = Building.objects.all()
    college = College.objects.all()
    rooms = rfilter.qs
    bcount = Building.objects.filter(college=college)

    context={'rooms':rooms,'filter':rfilter,'building':build,'colleges':college,'range':(0,)}
    return render(request,'UPM/room-view.html',context)
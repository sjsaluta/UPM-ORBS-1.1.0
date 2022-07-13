from distutils.command.build import build
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from . forms import *
from bookingapp.forms import *
from bookingapp.models import *
# Create your views here.

def indexPage(request):
    return redirect(dashBoardPage)

def dashBoardPage(request):
    return render(request,"base.html")

#### Admin Views #####

#manage terms
def manageTerm(request):
    terms = Term.objects.all()
    context={'terms':terms}
    return render(request,"UPM/term.html",context)

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
    print(room_term)
    if request.method == "POST":
        room = request.POST.getlist('rooms')
        for rm in room:
            if Room.objects.all().exists():
                rm = Room.objects.get(slug=rm)
                term.room.add(rm)
                return redirect(reverse('termView',kwargs={'slug':slug}))          
        if request.POST.get("activate"):
            term.isActivated=True
            term.save()
        elif request.POST.get("deactivate"):
            term.isActivated=False
            term.save()
        
    context ={'term':term,'rooms':rooms,'rms':room_term}
    return render(request,"UPM/term-details.html",context)

def addTerm(request):
    form = AddTerm()
    if request.method == "POST":
        form = AddTerm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-term.html",context)

#manage colleges
def manageCollege(request):
    colleges = College.objects.all()
    context={'colleges':colleges}
    return render(request,"UPM/college.html",context)

def addCollege(request):
    form = AddCollege()
    if request.method == "POST":
        form = AddCollege(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-college.html",context)

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

def addRoom(request):
    frbuild=False
    form = AddRoom()
    if request.method == "POST":
        form = AddRoom(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form,'frbuild':frbuild}
    return render(request,"UPM/add-room.html",context)

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

def calendarView(request, slug):
    room = Room.objects.get(slug=slug)
    terms = Term.objects.filter(room=room)
    term = None
    for t in terms:
        if t.isActivated:
            term = t

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

    context={'booking':booking,'room':room,'term':term,'form':form}
    return render(request,"UPM/calendar.html",context)


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

def buildingView(request,c,b):
    college = College.objects.get(slug=c)
    building= Building.objects.get(slug=b)
    room = building.room_set.all()
    context={'rooms':room,'building':building,'college':college}
    return render(request,'UPM/building-details.html',context)


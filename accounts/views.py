from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from . forms import *
# Create your views here.
def loginPage(request):
    iserror = False
    error=''
    if request.user.is_authenticated:
        return redirect('dashBoardPage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashBoardPage')
            else:
                iserror = True
                error = "There is no such user '" + username + "'."   
        context = {"error":error,"iserror":iserror}
        return render(request, 'accounts/login.html', context)

def logOutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def AddUserPage(request):
    add = False #add new fields
    form = CreateUserForm()
    ut = 0
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        role = request.POST.get('role')

        #gets the role from the select tag in template
        if role == 'faculty':
            ut=1
        elif role == 'staff':
            ut=2
        elif role == 'ocs':
            ut=3
        elif role == 'adpd':
            ut=4
        else:
            ut=5

        #adds user to database if form is valid
        if form.is_valid():
            user = form.save(False)
            user.user_type = ut
            user.save()
            
            #adds user to their respective roles
            if ut == 1:
                Faculty.objects.create(user=user,college=user.college,dept=user.department)
            elif ut == 2:
                Staff.objects.create(user=user,college=user.college,dept=user.department)
            elif ut == 3:
                OCS.objects.create(user=user,college=user.college)
            elif ut == 4:
                ADPD.objects.create(user=user)
            else:
                AO.objects.create(user=user)

    context = {'form': form,'add':add,'ut':ut}  
    
    
    return render(request,"accounts/add-user.html", context)

@login_required(login_url='loginPage')
def manageUsers(request):
    users = AuthUser.objects.exclude(username='admin')
    if request.method =="POST":
        role = request.POST.get('role')
        if role == 'faculty':
            users = AuthUser.objects.filter(user_type=1)
        elif role == 'staff':
            users = AuthUser.objects.filter(user_type=2)
        elif role == 'ocs':
            users = AuthUser.objects.filter(user_type=3)
        elif role == 'adpd':
            users = AuthUser.objects.filter(user_type=4)
        elif role == 'ao':
            users = AuthUser.objects.filter(user_type=5)
    context={'users':users}
    return render(request,"accounts/users.html",context)

def deleteUser(request,pk):
    user = AuthUser.objects.get(id=pk)
    user.delete()
    return redirect('manageUsers')
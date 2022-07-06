from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from . forms import *
# Create your views here.

def indexPage(request):
    return redirect(dashBoardPage)

def dashBoardPage(request):
    return render(request,"base.html")

def addTerm(request):
    form = AddTerm()
    if request.method == "POST":
        form = AddTerm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-term.html",context)

def addCollege(request):
    form = AddCollege()
    if request.method == "POST":
        form = AddCollege(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-college.html",context)

def addDept(request):
    form = AddDept()
    if request.method == "POST":
        form = AddDept(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-dept.html",context)

def addBuild(request):
    form = AddBuild()
    if request.method == "POST":
        form = AddBuild(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-build.html",context)

def addRoom(request):
    form = AddRoom()
    if request.method == "POST":
        form = AddRoom(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"UPM/add-room.html",context)
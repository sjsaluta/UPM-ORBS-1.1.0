from asyncio.windows_events import NULL
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from . forms import *

from bootstrap_modal_forms.generic import BSModalUpdateView,BSModalDeleteView


def loginPage(request):
    iserror = False
    error=''
    if request.user.is_authenticated:
        return redirect('indexPage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('indexPage')
            else:
                iserror = True
                error = "There is no such user '" + username + "'."   
        context = {"error":error,"iserror":iserror}
        return render(request, 'accounts/login.html', context)

def logOutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def viewProfile(request):
    user = request.user
    context = {'user':user}
    return render(request,'accounts/profile.html', context)

def editProfile(request):
    user= request.user
    form = EditUserForm(instance=user)

    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('profile'))

    context={'form':form}
    return render(request,'accounts/edit-profile.html',context)

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
            return redirect('manageUsers')

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

#update the table asynchronously
def users(request):
    data = dict()
    if request.method == 'GET':
        users = AuthUser.objects.exclude(username='admin')
        data['table'] = render_to_string(
            'accounts/user-table.html',
            {'users': users},
            request=request
        )
        return JsonResponse(data)

#edit user modal
def editUser(request,pk):
    user = AuthUser.objects.get(id=pk)
    if request.method == "POST":
        form= EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            
        return HttpResponseRedirect(reverse_lazy('manageUsers'))

    else:
        form = EditUserForm(instance=user)

        context = {'form': form,'u':user}
        return render(request, 'accounts/edit-user.html', context)

#change password modal
def changePass(request,pk):
    user = AuthUser.objects.get(id=pk)
    pw = PasswordChangeForm(user)
    if request.method == "POST":
        pw = PasswordChangeForm(data=request.POST, user=user)
        if pw.is_valid():
            pw.save()
            update_session_auth_hash(request, pw.user)
    context = {'pw': pw}
    return render(request, 'accounts/change-password.html', context)

#delete user modal
class deleteUser(BSModalDeleteView):
    model = AuthUser
    template_name = 'accounts/delete-user.html'
    success_message = 'Success: User was deleted.'
    success_url = reverse_lazy('manageUsers')

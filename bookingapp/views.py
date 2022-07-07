from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from . forms import *



# Create your views here.

def addBooking(request):
    form = AddBooking()
    user = request.user
    if request.method == "POST":
        form=AddBooking(request.POST)

        if form.is_valid():
            book=form.save(False)
            book.booker = user
            if(user.user_type == 1):
                book.faculty=user
                book.booker=user
            else:
                book.booker=user
            book.save()
    
    context={'form':form,'user':user}

    return render(request,'booking/add-booking.html',context)
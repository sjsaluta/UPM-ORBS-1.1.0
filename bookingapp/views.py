from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from . forms import *
from datetime import date



# Create your views here.

@login_required(login_url='loginPage')
def addBooking(request):
    form = AddBooking()
    user = request.user
    if request.method == "POST":
        form=AddBooking(request.POST)

        if form.is_valid():
            book=form.save(False)
            if(user.user_type == 1):
                book.faculty=user
                book.booker=user
            else:
                book.booker=user
            book.save()
    
    context={'form':form,'user':user}

    return render(request,'booking/add-booking.html',context)

@login_required(login_url='loginPage')
def viewBookings(request):
    bookings = Booking.objects.all()
    context={'bookings':bookings}
    return render(request, 'booking/booking.html',context)

@login_required(login_url='loginPage')
def bookingDetails(request,pk):
    booking = Booking.objects.get(id=pk)
    d = booking.start_time.strftime("%Y/%m/%d") + ' - ' + booking.end_time.strftime("%Y/%m/%d")
    time = booking.start_time.strftime("%I:%M%p") + '-' + booking.end_time.strftime("%I:%M%p")

    if request.POST.get("approve"):
        booking.isApproved=True
        booking.date_approved=date.today()
        if request.user.user_type is 5:
            booking.approver = request.user
        booking.save()

    context={'booking':booking,'date':d,'time':time}
    return render(request,'booking/booking-details.html',context)
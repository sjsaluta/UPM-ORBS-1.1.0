from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from . forms import *
from datetime import date



@login_required(login_url='loginPage')
def viewBookings(request):
    if request.user.user_type == 1 or request.user.user_type == 2:
        bookings = Booking.objects.filter(booker=request.user)
    else:
        bookings = Booking.objects.all()
    context={'bookings':bookings}
    return render(request, 'booking/booking.html',context)

@login_required(login_url='loginPage')
def bookingDetails(request,pk):
    booking = Booking.objects.get(id=pk)
    d = booking.start_time.strftime("%Y/%m/%d")
    time = booking.start_time.strftime("%I:%M%p") + '-' + booking.end_time.strftime("%I:%M%p")

    if request.POST.get("approve"):
        booking.isApproved=True
        booking.date_approved=date.today()
        if request.user.user_type == 5:
            booking.approver = AO.objects.get(user=request.user)
        booking.save()

    if request.method == "POST":
        remarks = request.POST.get('remarks')
        
        booking.remarks = remarks
        booking.save()
            
    context={'booking':booking,'date':d,'time':time}
    return render(request,'booking/booking-details.html',context)

#edit booking modal
def editBooking(request,pk):
    booking = Booking.objects.get(id=pk)
    form = AddBookFrCal(instance=booking)
    if request.method =="POST":
        form = AddBookFrCal(request.POST, instance = booking)

        if form.is_valid():
            form.save()
        
        return redirect(reverse('bookingDetails',kwargs={'pk':pk}))
    context = {'form':form}
    return render(request,'booking/edit-booking.html',context)

#update table asynchronously
def bookings(request,pk):
    data = dict()
    if request.method == 'GET':
        book = Booking.objects.all()
        data['table'] = render_to_string(
            'booking/booking-table.html',
            {'book': book},
            request=request
        )
        return JsonResponse(data)
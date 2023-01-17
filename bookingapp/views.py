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
from UPM.models import *



@login_required(login_url='loginPage')
def viewBookings(request):
    if request.user.user_type == 1 or request.user.user_type == 2:
        bookings = Booking.objects.filter(booker=request.user)
    elif request.user.user_type == None:
        bookings = Booking.objects.all()
    else:
        college = request.user.college
        print(college)
        bookings = Booking.objects.filter(room__college=college)
        
    context={'bookings':bookings}
    return render(request, 'booking/booking.html',context)

#Redirects to the detail page of the clicked booking schedule
@login_required(login_url='loginPage')
def bookingDetails(request,pk):
    
    booking = Booking.objects.get(id=pk)
    d = booking.start_time.strftime("%b %d %Y")
    time = booking.start_time.strftime("%I:%M%p") + '-' + booking.end_time.strftime("%I:%M%p")
    approve = request.POST.get("approve")
    reject = request.POST.get("reject")

    if request.method == "POST" and not approve and not reject:
        remarks = request.POST.get('remarks')
        booking.remarks = remarks
        booking.isEdited = False
        booking.save()

    elif approve:
        booking.isApproved=True
        booking.date_approved=date.today()
        booking.approver = ADPD.objects.get(user=request.user)
        booking.save()
    elif reject:
        booking.isApproved=False
        booking.save()
            
    context={'booking':booking,'date':d,'time':time}
    return render(request,'booking/booking-details.html',context)

#edit booking modal
def editBooking(request,pk):
    # room = Room.objects.get(slug=slug)
    booking = Booking.objects.get(id=pk)
    form = EditBookingForm(instance=booking)
    if request.method =="POST":
        form = EditBookingForm(request.POST, instance = booking)

        if form.is_valid():
            booking.isEdited=True
            booking.remarks = "Edited"
            form.save()
        
        return redirect(reverse('bookingDetails',kwargs={'pk':pk}))
    context = {'form':form}
    return render(request,'booking/edit-booking.html',context)

def deleteBooking(request,pk):
    booking = Booking.objects.get(id=pk)
    booking.delete()
    return redirect('viewBookings')


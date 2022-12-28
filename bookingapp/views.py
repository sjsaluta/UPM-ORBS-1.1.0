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


from bookingapp.filters import BookingFilter


@login_required(login_url='loginPage')
def viewBookings(request):
    if request.user.user_type == 1 or request.user.user_type == 2:
        bookings = Booking.objects.filter(booker=request.user)
        bfilter = BookingFilter(request.GET, queryset=bookings)
    elif request.user.user_type == None:
        bookings = Booking.objects.all()
        bfilter = BookingFilter(request.GET, queryset=bookings)
    else:
        college = request.user.college
        print(college)
        bookings = Booking.objects.filter(room__college=college)
        bfilter = BookingFilter(request.GET, queryset=bookings)

    context={'bookings':bookings, 'bfilter': bfilter}
    return render(request, 'booking/booking.html',context)

#Redirects to the detail page of the clicked booking schedule
@login_required(login_url='loginPage')
def bookingDetails(request,pk):
    
    booking = Booking.objects.get(id=pk)
    d = booking.start_time.strftime("%Y/%m/%d")
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

# Notification
@login_required(login_url='loginPage')
def viewNotif(request):
    booking = Booking.objects.filter(booker=request.user)
    approve = request.POST.get("approve")
    reject = request.POST.get("reject")

    user = request.user
    list_of_notifications = Notifications.objects.all()
    # unread_notifications = Notifications.objects.filter(user = request.user, is_opened = False).count()

    if approve:
        booking.isApproved=True
        booking.date_approved=date.today()
        booking.approver = ADPD.objects.get(user=request.user)

    elif reject:
        booking.isApproved=False
        

    context={'list_of_notifications':list_of_notifications, 'user':user} # 'unread_notifications':unread_notifications,
    return redirect(request, context)
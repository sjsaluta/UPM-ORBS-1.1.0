from django.db import models
from django.views.generic.list import ListView


from accounts.models import *
from UPM.models import *

# Create your models here.

class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    faculty =  models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True,blank = True)
    approver =  models.ForeignKey(ADPD,on_delete=models.CASCADE,null=True,blank=True)
    booker = models.ForeignKey(AuthUser,on_delete=models.CASCADE,null=True,blank=True)
    dept_or_office = models.CharField(max_length=300,null=True,blank=True)
    organization = models.CharField(max_length=300,null=True,blank=True)
    subject = models.CharField(max_length=300, null=True,blank=True)
    activity = models.CharField(max_length=300,null=True)
    isApproved = models.BooleanField(null=True, blank = True)
    isEdited = models.BooleanField(null=True, blank = True)
    date_approved = models.DateField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    numofstudents = models.IntegerField(null=True)
    equipment = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    #Get full name of user with email
    def getFullName(self):
        return self.faculty.user.first_name +' ' + self.faculty.user.last_name + ' (' + self.faculty.user.email + ')'
        
    def __str__(self):
        return "booking number " + str(self.id)

class Notifications(models.Model):
    is_opened = models.BooleanField(default=False)
    approved_disapproved = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE,null=True)

class NotificationListView(ListView):
    model = Notifications
    def get_queryset(self):
        return Notifications.objects.filter(user=self.request.user).order_by("-timestamp")

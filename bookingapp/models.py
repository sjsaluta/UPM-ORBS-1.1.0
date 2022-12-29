from django.db import models

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
    #start_time = models.DateTimeField(null=True)#OLD
    #end_time = models.DateTimeField(null=True)#OLD
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    date_picked = models.DateField(null=True)
    numofstudents = models.IntegerField(null=True)
    equipment = models.ManyToManyField(Equipment) #Room.equipment
    remarks = models.TextField(null=True, blank=True)
 
    #Get full name of user with email
    def getFullName(self):
        return self.faculty.user.first_name +' ' + self.faculty.user.last_name + ' (' + self.faculty.user.email + ')'
        
    def __str__(self):
        return "booking number " + str(self.id)


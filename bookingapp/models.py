from django.db import models

from accounts.models import *
from UPM.models import *

# Create your models here.

class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    faculty =  models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True)
    approver =  models.ForeignKey(ADPD,on_delete=models.CASCADE,null=True,blank=True)
    booker = models.ForeignKey(AuthUser,on_delete=models.CASCADE,null=True,blank=True)
    subject = models.CharField(max_length=300, null=True)
    activity = models.CharField(max_length=300,null=True)
    isApproved = models.BooleanField(default=False)
    date_approved = models.DateField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    date = models.DateField(null=True)
    isRecurring = models.BooleanField(default=False)
    numofstudents = models.IntegerField(null=True)

    def __str__(self):
        return "booking number " + str(self.id)
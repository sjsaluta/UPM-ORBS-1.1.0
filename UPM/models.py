from django.db import models
from accounts.models import *

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=300,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=300,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=300,null=True)
    
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    isAvailable = models.BooleanField(default=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Term(models.Model):
    academicyear = models.CharField(max_length=10)
    room = models.ManyToManyField(Room, related_name="room_term")
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    def __str__(self):
        return self.academicyear

class Schedule(models.Model):
    DAYS_OF_WEEK = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
    )

    term = models.ForeignKey(Term,on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    faculty = models.ForeignKey("accounts.Faculty",on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=200,null=True)
    time_start=models.DateTimeField(null=True)
    time_end=models.DateTimeField(null=True)
    dayofweek = models.PositiveSmallIntegerField(choices=DAYS_OF_WEEK,null=True)
    

    def __str__(self):
        return "Schedule " + self.id
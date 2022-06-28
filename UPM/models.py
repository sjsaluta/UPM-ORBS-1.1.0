from django.db import models

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
class Term(models.Model):
    academicyear = models.CharField(max_length=10)

    def __str__(self):
        return self.academicyear

class Room(models.Model):
    name = models.CharField(max_length=300,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    isAvailable = models.BooleanField(default=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Schedule(models.Model):
    term = models.ForeignKey(Term,on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return "Schedule" + self.id
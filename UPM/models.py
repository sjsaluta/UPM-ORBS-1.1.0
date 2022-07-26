from django.db import models
from accounts.models import *
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=300,null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("collegeView", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Department(models.Model):
    name = models.CharField(max_length=300,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Building(models.Model):
    name = models.CharField(max_length=300,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Room(models.Model):
    TYPES = (
        (1,"Room"),
        (2,"Theatre"),
    )

    name = models.CharField(max_length=300,null=True, unique=True)
    slug = models.SlugField(null=True)
    room_type =models.PositiveSmallIntegerField(choices=TYPES,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Term(models.Model):
    academicyear = models.CharField(max_length=10)
    slug = models.SlugField(null=True)
    room = models.ManyToManyField(Room, related_name="room_term", blank=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    isActivated = models.BooleanField(null=True,default=False)

    def __str__(self):
        return self.academicyear

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify('term'+self.name)
        return super().save(*args, **kwargs)

class ScheduleFile(models.Model):
    term = models.ForeignKey(Term,on_delete=models.CASCADE,null=True)
    college = models.OneToOneField(College,on_delete=models.CASCADE,null=True)
    ocs = models.ForeignKey('accounts.OCS', on_delete=models.CASCADE,null=True)
    file = models.FileField()

    def __str__(self):
        return str(self.file)

class Schedule(models.Model):
    schedfile = models.ForeignKey(ScheduleFile,on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    faculty = models.CharField(max_length=200,null=True)
    coursetitle= models.CharField(max_length=200,null=True)
    classnum = models.IntegerField(null=True)
    component = models.CharField(max_length=10,null=True)
    section = models.CharField(max_length=10,null=True)
    subject = models.CharField(max_length=200,null=True)
    capacity= models.IntegerField(null=True)
    time_start= models.TimeField(null=True)
    time_end= models.TimeField(null=True)
    dayofweek = models.CharField(max_length=10,null=True)
    

    def __str__(self):
        return self.coursetitle + ' - ' + self.section  + ' - ('+ self.component + ')'

    def getDays(self):
        arr=[]
        arr[:0]=self.dayofweek
        arr = [int(i) for i in arr]
        return arr

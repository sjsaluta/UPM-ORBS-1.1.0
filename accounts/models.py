from time import timezone
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from UPM.models import *


# Create your models here.
class AuthUser(AbstractUser):
    FACULTY = 1
    STAFF = 2
    OCS = 3
    ADPD = 4
    USER_TYPE_CHOICES = (
        (FACULTY, 'faculty'),
        (STAFF, 'staff'),
        (OCS, 'ocs'),
        (ADPD, 'adpd'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)
    def __str__(self):
        return f"{self.username}"

class Faculty(models.Model):
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=300,null=True)
    last_name=models.CharField(max_length=300,null=True)
    email=models.EmailField(max_length=50,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name_plural = "Faculties"

class OCS(models.Model):
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=300,null=True)
    last_name=models.CharField(max_length=300,null=True)
    email=models.EmailField(max_length=50,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name_plural = "College Secretaries"

class Staff(models.Model):
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=300,null=True)
    last_name=models.CharField(max_length=300,null=True)
    email=models.EmailField(max_length=50,null=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)

class ADPD(models.Model):
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=300,null=True)
    last_name=models.CharField(max_length=300,null=True)
    email=models.EmailField(max_length=50,null=True)

    class Meta:
        verbose_name_plural = "ADPDs"


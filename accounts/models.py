from time import timezone
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from UPM.models import *



class AuthUser(AbstractUser):
    """creates user_types for all users"""
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
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, validators=[
        EmailValidator(allowlist=['up.edu.ph'])
    ])
    college = models.ForeignKey("UPM.College",on_delete=models.CASCADE,null=True,blank=True)
    department = models.ForeignKey("UPM.Department",on_delete=models.CASCADE,null=True,blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)
    def __str__(self):
        return self.username

class Faculty(models.Model):
    user = models.OneToOneField(AuthUser,on_delete=models.CASCADE,null=True)
    college = models.ForeignKey("UPM.College",on_delete=models.CASCADE,null=True)
    dept = models.ForeignKey("UPM.Department",on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        name = AuthUser.get_full_name(self.user)
        return name + ' <' + self.user.email + '>'

class OCS(models.Model):
    user = models.OneToOneField(AuthUser,on_delete=models.CASCADE,null=True)
    college = models.ForeignKey("UPM.College",on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name_plural = "College Secretaries"

    def __str__(self):
        name = AuthUser.get_full_name(self.user)
        return name + ' <' + self.user.email + '>'

class Staff(models.Model):
    user = models.OneToOneField(AuthUser,on_delete=models.CASCADE,null=True)

    college = models.ForeignKey("UPM.College",on_delete=models.CASCADE,null=True)
    dept = models.ForeignKey("UPM.Department",on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        name = AuthUser.get_full_name(self.user)
        return name + ' <' + self.user.email + '>'

class ADPD(models.Model):
    user = models.OneToOneField(AuthUser,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=300,null=True)
    last_name=models.CharField(max_length=300,null=True)
    email=models.EmailField(max_length=50,null=True)

    class Meta:
        verbose_name_plural = "ADPDs"

    def __str__(self):
        name = AuthUser.get_full_name(self.user)
        return name + ' <' + self.user.email + '>'

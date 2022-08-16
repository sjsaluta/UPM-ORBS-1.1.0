from django import forms
from django.forms import DateInput
from django.utils.translation import gettext_lazy as _
from django.forms import ModelChoiceField, ModelForm,EmailField
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
from .widgets import *


class AddBookFrCal(ModelForm):
    class Meta:
        model = Booking
        fields = ['faculty','subject','start_time','end_time','numofstudents','activity','equipment','dept_or_office','organization']

        labels={
            'numofstudents':'Number of Students',
            'start_time':'Start Time',
            'end_time':'End Time',
            'dept_or_office':'Dept/Office'
        }
        widgets={
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ), 
        }

class EditBookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['faculty','subject','start_time','end_time','numofstudents','activity','equipment','dept_or_office','organization','room']

        labels={
            'numofstudents':'Number of Students',
            'start_time':'Start Time',
            'end_time':'End Time',
            'dept_or_office':'Dept/Office'
        }
        widgets={
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ), 
        }
class RemarksForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['remarks']
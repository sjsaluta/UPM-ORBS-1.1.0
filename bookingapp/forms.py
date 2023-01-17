from django import forms
from django.forms import DateInput
from django.forms import TimeInput#New
from django.utils.translation import gettext_lazy as _
from django.forms import ModelChoiceField, ModelForm,EmailField
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
from .widgets import *
from UPM.models import *


class AddBookFrCal(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        room_id = kwargs.pop('room_id')
        super(AddBookFrCal, self).__init__(*args, **kwargs)
        room = Room.objects.get(pk=room_id)
        self.fields['equipment'] = forms.ModelMultipleChoiceField(
            queryset = room.equipment.all(),
            widget = forms.CheckboxSelectMultiple,
            required=False,
        )
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
            "start_time": DateInput(#DateTimeInput
                attrs={"type": "datetime-local", "class": "form-control"},#"type": "datetime-local"
                format="%Y-%m-%dT%H:%M",
                #format="T%H:%M",
            ),
            "end_time": DateInput(#DateTimeInput
                attrs={"type": "datetime-local", "class": "form-control"},#"type": "datetime-local"
                format="%Y-%m-%dT%H:%M",
            ),
        }

class EditBookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ['faculty','subject','start_time','end_time','numofstudents','activity','dept_or_office','organization','room']

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

from cProfile import label
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelChoiceField, ModelForm,EmailField
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
import json

class AddTerm(ModelForm):
    date_start = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    date_end = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Term
        fields = ['academicyear','date_start','date_end']

        labels={
            'academicyear':'Academic Year',
            'date_start':'Starting Date',
            'date_end':'End Date',
        }
class AddCollege(ModelForm):
    class Meta:
        model = College
        fields = ['name']

class AddBuild(ModelForm):
    class Meta:
        model = Building
        fields = ['name']

class AddDept(ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class AddRoom(ModelForm):
    class Meta:
        model = Room
        fields = ['name','capacity','room_type']

class AddTermRoom(ModelForm):
    class Meta:
        model = Term
        fields = ['room']

class ColBuildForm(ModelForm):

    class Meta:
        model = Room
        fields = ('college','building','name','capacity','room_type')

class UploadForm(ModelForm):

    class Meta:
        model= ScheduleFile
        fields = ('term','file')
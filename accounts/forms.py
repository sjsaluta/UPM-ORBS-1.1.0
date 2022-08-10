from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelChoiceField, ModelForm,EmailField
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

from bootstrap_modal_forms.forms import PopRequestMixin,CreateUpdateAjaxMixin

class CreateUserForm(UserCreationForm):
    
    email = EmailField()
    
    #only allow @up.edu.ph emails
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@up.edu.ph" not in data:   # any check you need
            raise forms.ValidationError("Must be a UP email address (up.edu.ph)")
        return data

    class Meta:
        model = AuthUser
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2','college','department']

class EditUserForm(UserChangeForm):

    class Meta:
        model= AuthUser
        fields = ['first_name','last_name','username','password','college','department']
from django import forms
from localflavor.au.forms import AUPhoneNumberField, AUPostCodeField
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserType

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = ('street_num_name', 'suburb', 'postcode', 'phone_number')

'''class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email_address', 'street_num_name', 'suburb', 'postcode', 'phone_number']'''

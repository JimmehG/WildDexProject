from django import forms
from localflavor.au.forms import AUPhoneNumberField, AUPostCodeField
from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email_address', 'street_num_name', 'suburb', 'postcode', 'phone_number']

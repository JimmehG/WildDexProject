from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserType, Animal


class CarerForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserType
        fields = ['first_name', 'last_name', 'email', 'street_num_name', 'suburb', 'postcode', 'phone_number']

'''class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email_address', 'street_num_name', 'suburb', 'postcode',
         'phone_number']'''


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['caller_name', 'caller_number', 'street_num_name', 'suburb', 'postcode', 'species',
                  'gender', 'encounter_date', 'encounter_location', 'care_purpose', 'status',
                  'branch_coordinator', 'office_volunteer']


class AnimalFormCarer(ModelForm):
    class Meta:
        model = Animal
        fields = ['species', 'gender', 'encounter_date', 'encounter_location', 'care_purpose', 'status',
                  'branch_coordinator']

from django import forms
from django.forms import ModelForm
from .models import UserType, Animal, Carer, BranchCoordinator, OfficeVolunteer


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserType
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'street_num_name', 'suburb', 'postcode',
                  'phone_number', 'b_branch_c',
                  'b_office', 'b_carer']


class BranchCForm(ModelForm):
    class Meta:
        model = BranchCoordinator
        fields = ['branch', 'specialty', 'facilities', 'vaccinations']


class CarerForm(ModelForm):
    class Meta:
        model = Carer
        fields = ['branch_coordinator', 'specialty', 'facilities', 'vaccinations']


class OfficeForm(ModelForm):
    class Meta:
        model = OfficeVolunteer
        fields = '__all__'


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

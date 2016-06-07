from django import forms
from django.forms import ModelForm
from .models import UserType, Animal, Carer, BranchCoordinator, OfficeVolunteer, UserTypeTemp, RegisterUser


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserType
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'address', 'suburb', 'postcode',
                  'phone_number']


class UserFormTemp(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserTypeTemp
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


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
        fields = '__all__'


class AnimalFormCarer(ModelForm):
    class Meta:
        model = Animal
        exclude = ['status', 'carer', 'office_volunteer', 'branch_coordinator', 'assessed', 'picked_up']


class IDForm(forms.Form):
    register_id = forms.CharField()


class NewUserForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = ['b_branch_c', 'b_office', 'b_carer']

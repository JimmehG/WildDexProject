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
    # carer = forms.ModelChoiceField(queryset='carer', to_field_name='id')
    # branch_coordinator = forms.ModelChoiceField(queryset='branch_coordinator', to_field_name='id')
    encounter_date = forms.DateField(input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'])

    class Meta:
        model = Animal
        fields = ['species', 'caller_address', 'caller_name', 'caller_number', 'suburb', 'postcode', 'encounter_date',
                  'encounter_location', 'injury_description', 'age', 'carer', 'branch_coordinator']


class AnimalFormCarer(ModelForm):
    # carer = forms.ModelChoiceField(queryset='carer', to_field_name='id')
    # branch_coordinator = forms.ModelChoiceField(queryset='branch_coordinator', to_field_name='id')
    encounter_date = forms.DateField(input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y'])

    class Meta:
        model = Animal
        fields = ['species', 'caller_address', 'caller_name', 'caller_number', 'suburb', 'postcode', 'encounter_date',
                  'encounter_location', 'age', 'weight', 'picture', 'status_detail',
                  'injury', 'cause_of_injury']


class IDForm(forms.Form):
    register_id = forms.CharField()


class NewUserForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = ['b_branch_c', 'b_office', 'b_carer']

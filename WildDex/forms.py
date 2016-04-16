from django import forms
from localflavor.au.forms import AUPhoneNumberField, AUPostCodeField
from django import newform as forms
from address.forms import AddressField


class PersonForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=64)
    last_name = forms.CharField(label='Last Name', max_length=64)
    street_num_name = forms.CharField(label='Street Number and Name', max_length=64)
    suburb = forms.CharField(label='Suburb', max_length=64)
    postcode = AUPostCodeField()
    phone_number = AUPhoneNumberField()

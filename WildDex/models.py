from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField


# Create your models here.
# ID CREATED AUTOMATICALLY. as id = models.AutoField(primary_key=True)

class Animal(models.Model):
    SPECIES_CHOICES = (
        ('RTP', 'Ring Tail Possum'),
        # add species in here
    )
    species = models.CharField(max_length=64, choices=SPECIES_CHOICES)
    caller = models.ForeignKey('Caller',
                               on_delete=models.SET_NULL,
                               null=True, )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    prev_carers = models.ManyToManyField('Carer')


class Caller(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = PhoneNumberField()
    address = AddressField()


class Branch(models.Model):
    address = AddressField()
    phone_number = PhoneNumberField()


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.EmailField()
    phone_number = PhoneNumberField()


class OfficeVolunteer(User):
    pass


class Carer(User):
    address = AddressField()
    animals = models.ManyToManyField('Animal')


class BranchManager(User):
    pass

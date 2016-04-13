from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
# ID CREATED AUTOMATICALLY.

class Animal(models.Model):
    SPECIES_CHOICES = (
        ('RTP', 'Ring Tail Possum'),
        # add species in here
    )
    species = models.CharField(max_length=64,choices=SPECIES_CHOICES)
    caller_first_name = models.CharField(max_length=64)
    caller_last_name = models.CharField(max_length=64)
    caller_phone_number = PhoneNumberField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # prev_owners = needs array of previous owners


class OfficeVolunteer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.EmailField()
    phone_number = PhoneNumberField()


class Carer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.EmailField()
    phone_number = PhoneNumberField()


class BranchManager(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.EmailField()
    phone_number = PhoneNumberField()
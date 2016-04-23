from django.db import models
from localflavor.au.models import AUPhoneNumberField, AUPostCodeField
from django.contrib.auth.models import User

# from address.models import AddressField CHANGE ADDRESS TO LOCALFLAVOR AND CHARFIELDS


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
    phone_number = AUPhoneNumberField()
    # address = AddressField()


class Branch(models.Model):
    # address = AddressField()
    phone_number = AUPhoneNumberField()


class UserType(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
   # User model in Django already has email, username and password attributes
   # first_name = models.CharField(max_length=64)
   # last_name = models.CharField(max_length=64)
   # email_address = models.EmailField()
    phone_number = AUPhoneNumberField(blank=True)
    street_num_name = models.CharField(max_length=256,blank=True)
    suburb = models.CharField(max_length=64,blank=True)
    postcode = AUPostCodeField(max_length=8,blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
"""def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(
            self, self.first_name, self.last_name, self.email_address,
            self.phone_number, self.street_num_name, self.suburb, self.postcode) """


class OfficeVolunteer(User):
    pass


class Carer(User):
    # address = AddressField()
    animals = models.ManyToManyField('Animal')


class BranchManager(User):
    pass

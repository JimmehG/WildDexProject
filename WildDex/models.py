from django.db import models
from localflavor.au.models import AUPhoneNumberField, AUPostCodeField
from django.contrib.auth.models import User

# from address.models import AddressField CHANGE ADDRESS TO LOCALFLAVOR AND CHARFIELDS


# Create your models here.
# ID CREATED AUTOMATICALLY. as id = models.AutoField(primary_key=True)

class Animal(models.Model):
    SPECIES_CHOICES = (
        ('RTP', 'Ringtail Possum'),
        ('RLK', 'Rainbow Lorrikeet'),
        ('TFM', 'Tawny Frogmouth'),
        ('BTP', 'Brushtail Possum'),
        ('GFF', 'Grey-headded Flying Fox')
    )
    species = models.CharField(max_length=64, choices=SPECIES_CHOICES, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    prev_carers = models.ManyToManyField('Carer', blank=True)
    caller_name = models.CharField(max_length=128, blank=False, null=True)
    caller_number = AUPhoneNumberField(blank=False, null=True)
    street_num_name = models.CharField(max_length=256, blank=False, null=True)
    suburb = models.CharField(max_length=64, blank=False, null=True)
    postcode = AUPostCodeField(max_length=8, blank=True)
    encounter_location = models.CharField(max_length=256, blank=True)
    encounter_date = models.DateField(blank=False, null=True)
    care_purpose = models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, blank=True)
    branch_coordinator = models.ForeignKey('BranchCoordinator', on_delete=models.SET_NULL, null=True, blank=True)
    office_volunteer = models.ForeignKey('OfficeVolunteer', on_delete=models.SET_NULL, null=True, blank=True)


class UserType(User):
    phone_number = AUPhoneNumberField(blank=False, null=True)
    street_num_name = models.CharField(max_length=256, blank=False, null=True)
    suburb = models.CharField(max_length=64, blank=False, null=True)
    postcode = AUPostCodeField(max_length=8, blank=False, null=True)
    availabilities = models.CharField(max_length=128, blank=False, null=True)
    b_office = models.BooleanField()
    b_carer = models.BooleanField()
    b_branch_c = models.BooleanField()
    office = models.OneToOneField('OfficeVolunteer', null=True, on_delete=models.CASCADE)
    carer = models.OneToOneField('Carer', null=True, on_delete=models.CASCADE)
    branch_c = models.OneToOneField('BranchCoordinator', null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.username


class OfficeVolunteer(models.Model):
    office_number = AUPhoneNumberField(blank=False, null=True)


class Carer(models.Model):
    animals = models.ManyToManyField('Animal')
    branch_coordinator = models.ForeignKey('BranchCoordinator', on_delete=models.SET_NULL, null=True)
    specialty = models.CharField(max_length=128, blank=True)
    facilities = models.CharField(max_length=128, blank=True)
    vaccinations = models.CharField(max_length=128, blank=True)


class BranchCoordinator(models.Model):
    branch = models.CharField(max_length=128, blank=True)
    animals = models.ManyToManyField('Animal')
    specialty = models.CharField(max_length=128, blank=True)
    facilities = models.CharField(max_length=128, blank=True)
    vaccinations = models.CharField(max_length=128, blank=True)


'''class Branch(models.Model):
    street_num_name = models.CharField(max_length=256, blank=False, null=True)
    suburb = models.CharField(max_length=64, blank=False, null=True)
    postcode = AUPostCodeField(max_length=8, blank=False, null=True)
    phone_number = AUPhoneNumberField(blank=False, null=True)'''

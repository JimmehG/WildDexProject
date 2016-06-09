from django.db import models
from localflavor.au.models import AUPhoneNumberField, AUPostCodeField
from django.contrib.auth.models import User


# from address.models import AddressField CHANGE ADDRESS TO LOCALFLAVOR AND CHARFIELDS


# Create your models here.
# ID CREATED AUTOMATICALLY. as id = models.AutoField(primary_key=True). can be accessed with .pk or .id

class Animal(models.Model):
    SPECIES_CHOICES = (
        ('RTP', 'Ringtail Possum'),
        ('RLK', 'Rainbow Lorrikeet'),
        ('TFM', 'Tawny Frogmouth'),
        ('BTP', 'Brushtail Possum'),
        ('GFF', 'Grey-headded Flying Fox')
    )
    species = models.CharField(max_length=3, choices=SPECIES_CHOICES, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    caller_name = models.CharField(max_length=64, blank=False, null=True)
    caller_number = AUPhoneNumberField(blank=False, null=True)
    caller_address = models.CharField(max_length=128, blank=False, null=True)
    suburb = models.CharField(max_length=64, blank=False, null=True)
    postcode = AUPostCodeField(max_length=8, blank=True)
    encounter_location = models.CharField(max_length=128, blank=True)
    encounter_date = models.DateField(blank=False, null=True)
    injury_description = models.CharField(max_length=256, blank=True)
    INJURY_CHOICES = (
        (0, 'Concussion/Stunned'),
        (1, 'Deformity'),
        (2, 'Feather Problem'),
        (3, 'Skin Problem'),
        (4, 'Gastric/Digestive'),
        (5, 'Body Injury'),
        (6, 'Eye Injury'),
        (7, 'Fore Limb/Wing Injury'),
        (8, 'Rear Limb/Injury'),
        (9, 'Head Injury'),
        (10, 'Neck Injury'),
        (11, 'Tail Injury'),
        (12, 'Nothing Apparent'),
        (13, 'Covered in Oil,ETC'),
        (14, 'Separated from Parents'),
        (15, 'Undernourished/Exhausted'),
    )
    injury = models.IntegerField(blank=True, choices=INJURY_CHOICES)
    CAUSE_CHOICES = (
        (0, 'Cat Attack'),
        (1, 'Dog Attack'),
        (2, 'Other Animal Attack'),
        (3, 'Collision(e.g.Window)'),
        (4, 'Motor Vehicle'),
        (5, 'Domestic Escape/Release'),
        (6, 'Runner Disease'),
        (7, 'Other Disease'),
        (8, 'Electrocution'),
        (9, 'Entangled'),
        (10, 'Fire'),
        (11, 'Fallen'),
        (12, 'Geriatric'),
        (13, 'Human Interference'),
        (14, 'Habitat Lost'),
        (15, 'Oil/Chemical/Poison'),
        (16, 'Unsuitable Environment'),
        (17, 'Weather(Beach Washed,ETC)'),
        (18, 'Unknown'),
    )
    cause_of_injury = models.IntegerField(blank=True, choices=CAUSE_CHOICES)
    STATUS_CHOICES = (
        (0, 'Humanely euthanased'),
        (1, 'In Care'),
        (2, 'Relocated'),
        (3, 'No action'),
    )
    status = models.IntegerField(null=True, blank=True, choices=STATUS_CHOICES)
    status_detail = models.CharField(max_length=256, blank=True)
    status_date = models.DateField(blank=True, null=True)
    carer = models.ForeignKey('Carer', on_delete=models.SET_NULL, null=True, blank=True)
    # TODO prev_carers = models.ManyToManyField('Carer', blank=True) SORRY NO PREVIOUS CARERS FOR NOW
    branch_coordinator = models.ForeignKey('BranchCoordinator', on_delete=models.SET_NULL, null=True, blank=True)
    office_volunteer = models.ForeignKey('OfficeVolunteer', on_delete=models.SET_NULL, null=True, blank=True)
    picture = models.ImageField(upload_to='animal_pictures', null=True, blank=True)
    weight = models.FloatField(max_length=10, blank=True, null=True)
    AGE_CHOICES = (
        (0, 'Baby'),
        (1, 'Juvenile'),
        (2, 'Adult')
    )
    age = models.IntegerField(choices=AGE_CHOICES, blank=True, null=True)
    assessed = models.BooleanField(default=False)
    picked_up = models.BooleanField(default=False)


class UserType(User):
    phone_number = AUPhoneNumberField(blank=False, null=True)
    address = models.CharField(max_length=256, blank=False, null=True)
    suburb = models.CharField(max_length=64, blank=False, null=True)
    postcode = AUPostCodeField(max_length=8, blank=False, null=True)
    availabilities = models.CharField(max_length=128, blank=False, null=True)
    b_office = models.BooleanField()
    b_carer = models.BooleanField()
    b_branch_c = models.BooleanField()
    office = models.OneToOneField('OfficeVolunteer', null=True, on_delete=models.CASCADE)
    carer = models.OneToOneField('Carer', null=True, on_delete=models.CASCADE)
    branch_c = models.OneToOneField('BranchCoordinator', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class UserTypeTemp(User):
    b_office = models.BooleanField()
    b_carer = models.BooleanField()
    b_branch_c = models.BooleanField()
    office = models.OneToOneField('OfficeVolunteer', null=True, on_delete=models.CASCADE)
    carer = models.OneToOneField('Carer', null=True, on_delete=models.CASCADE)
    branch_c = models.OneToOneField('BranchCoordinator', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class OfficeVolunteer(models.Model):
    office_number = AUPhoneNumberField(blank=False, null=True)

    def __str__(self):
        return u'{0} {1} ({2})'.format(self.usertypetemp.first_name,
                                       self.usertypetemp.last_name, self.usertypetemp.username)


class Carer(models.Model):
    branch_coordinator = models.ForeignKey('BranchCoordinator', on_delete=models.SET_NULL, null=True)
    specialty = models.CharField(max_length=128, blank=True)
    facilities = models.CharField(max_length=128, blank=True)
    vaccinations = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return u'{0} {1} ({2})'.format(self.usertypetemp.first_name,
                                       self.usertypetemp.last_name, self.usertypetemp.username)


class BranchCoordinator(models.Model):
    branch = models.CharField(max_length=128, blank=True)
    specialty = models.CharField(max_length=128, blank=True)
    facilities = models.CharField(max_length=128, blank=True)
    vaccinations = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return u'{0} {1} ({2})'.format(self.usertypetemp.first_name,
                                       self.usertypetemp.last_name, self.usertypetemp.username)


class RegisterUser(models.Model):
    used = models.BooleanField(default=False)
    b_office = models.BooleanField()
    b_carer = models.BooleanField()
    b_branch_c = models.BooleanField()

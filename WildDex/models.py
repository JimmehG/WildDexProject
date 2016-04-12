from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
# ID CREATED AUTOMATICALLY.

class Animal(models.Model):
    species = models.CharField(max_length=64)
    # prev_owners = needs array of previous owners


class Caller(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = PhoneNumberField()

from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

#Profile Database
class Profile(models.Model):
    GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
    )

    PROGRAMME = (
        ('bt', 'B.Tech'),
        ('mt', 'M.Tech'),
        ('phd', 'PhD'),
        ('bd', 'B.Des'),
        ('md', 'M.Des'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name="First Name",max_length=50)
    last_name = models.CharField(verbose_name="Last name",max_length=50)
    roll_no = models.CharField(verbose_name="Roll Number", max_length=8, unique=True, default = 2019352)
    dob = models.DateField(verbose_name="Date of Birth", null = True)
    batch = models.IntegerField(null = True)
    programme = models.CharField(max_length=3, choices=PROGRAMME, default = 'bt')
    gender = models.CharField(max_length=1, choices=GENDER)
    alt_email = models.EmailField(verbose_name="Alternate Email", max_length=255, blank=True)
    contact_no = models.CharField(verbose_name="Contact Number", max_length=13)
    street_address1 = models.CharField(verbose_name="Address Line 1", max_length=255)
    street_address2 = models.CharField(verbose_name="Address Line 2", max_length=255, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name +"  "+ str(self.user)
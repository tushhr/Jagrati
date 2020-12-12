from django.db import models
from django.utils import timezone
from django.utils.timezone import now 
import datetime
from django.db import models
from PIL import Image

from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.
class events(models.Model):

	"""docstring for  events"""
	event_name=models.CharField(max_length = 50, verbose_name = 'Event', default = 'Invicta')
	date = models.DateField()
	venue = models.CharField(max_length = 50, verbose_name = 'venue', default = 'In front of Audi')
	description = models.CharField(max_length = 200, default = 'Fun event')
	organiser = models.ManyToManyField(Profile)
	winner1 = models.CharField(max_length = 20, null = True, blank = True)
	image = models.ImageField(null = True, upload_to ='events/')


	def __str__(self):
		return self.event_name +" on "+ str(self.date)[0:10]
		
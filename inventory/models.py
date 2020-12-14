from django.db import models
from django.utils import timezone
from django.utils.timezone import now 
import datetime

#from accounts.models import profile
# Create your models here.

#all donation transaction
class asset_donation(models.Model):
	
	"""docstring for asset"""
	asset_name = models.CharField(verbose_name = 'Asset', max_length = 20, default = 'bags', null = False)
	donated_by = models.CharField(verbose_name = 'Donated By', max_length = 20)
	quantity = models.IntegerField(default = 1, null = False)
	date = models.DateTimeField(default=now)
	
	def __str__(self):
		return self.asset_name+" by "+ str(self.donated_by)

#all assets databse
class asset(models.Model):

	"""docstring for asset"""
	asset_name = models.CharField(db_column = 'asset_name', max_length = 20, default = 'bags', null = False)
	quantity = models.IntegerField(default = 1, null = False)
	
	def __str__(self):
		return self.asset_name

#all withdrawn transaction
class asset_transaction(models.Model):
	
	"""docstring for asset"""
	asset_name = models.CharField( max_length = 20, default = 'bags', null = False)
	volunteer = models.CharField(verbose_name = 'volunteer', max_length = 20)
	quantity = models.IntegerField()
	date = models.DateTimeField(default = now)

	def __str__(self):
		return self.asset_name

	
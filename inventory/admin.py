from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(asset_donation)
admin.site.register(asset)
admin.site.register(asset_transaction)

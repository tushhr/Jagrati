from django.contrib import admin
from django.urls import path, include
from . import views

app_name='inventory'

urlpatterns = [
	path('', views.index, name='inventory'),
	#if someone add item in inventory
	path('add', views.add_item, name='add'),
	#if someone removes item from inventory
	path('withdraw', views.withdraw, name='withdraw'),
]
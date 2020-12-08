from django.contrib import admin
from django.urls import path, include
from . import views

app_name='events'

urlpatterns = [
    path('', views.index, name='events'),
    path('new_event', views.new_event, name='new_event'),
    path('add', views.add, name='add-event'),
]

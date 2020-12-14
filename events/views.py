from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login as auth_login, logout
from datetime import datetime

from django.contrib.auth.models import User
from .models import events
from accounts.models import Profile

# Create your views here.
#Home Page
@login_required
def index(request):

	data_old = events.objects.filter(date__lt = datetime.now())
	data_new = events.objects.filter(date__gte = datetime.now())
	
	context={'data_old': data_old, 'data_new':data_new}

	current_user = request.user
	
	#if profile is complete redirect to events else redirect to complete profile page	
	if Profile.objects.filter(user = current_user).exists():
		return render(request, 'events/home.html', context)
	else:
		return redirect('/accounts/create')

@login_required
def new_event(request):
	current_user = request.user
	
	#if profile is complete redirect to events else redirect to complete profile page	
	if Profile.objects.filter(user = current_user).exists():
		return render(request, 'events/add_event.html')
	else:
		return redirect('/accounts/create')

#To add an event
def add(request):

	#Add an event
	if request.method == "POST":
		event_name=request.POST['event_name']
		date=request.POST['date']
		venue=request.POST['venue']
		description=request.POST['description']
		organiser1=request.POST['organiser1']
		winner1=request.POST['winner1']
		image = request.FILES['image']

		event = events(event_name = event_name, date = date, venue = venue, description = description, winner1 = winner1, image = image)
		event.save()
		event.organiser.add(Profile.objects.get(roll_no = organiser1))
		
		event.save()
		messages.success(request, "Done Successfully!")
		return redirect('/')


	return render(request, 'events/add_event.html')


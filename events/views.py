from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login as auth_login, logout
from django.contrib.auth.models import User

from .models import events
from accounts.models import Profile

# Create your views here.
#Home Page
@login_required
def index(request):
	current_user = request.user
	
	#if profile is complete redirect to events else redirect to complete profile page	
	if Profile.objects.filter(user = current_user).exists():
		return render(request, 'events/home.html')
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
		#if there is an co-host
		if request.POST['organiser2'] is not None:
			organiser2 = request.POST['organiser2']
		winner1=request.POST['winner1']
		winner2=request.POST['winner2']
		winner3=request.POST['winner3']

		#check whether event with same name exist or not
		if events.objects.filter(event_name = event_name).exists():
			messages.error(request, "Event with same name already exist!")
		else:
			event = events(event_name = event_name, date = date, venue = venue, description = description, winner1 = winner1, winner3 = winner3, winner2 = winner2)
			event.save()
			event.organiser.add(Profile.objects.get(roll_no = organiser1))
			if organiser2:
				event.organiser.add(Profile.objects.get(roll_no = organiser2))

			event.save()
			messages.error(request, "Done Successfully!")
			return redirect('')


	return render(request, 'events/add.html')


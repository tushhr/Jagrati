from django.shortcuts import render,  redirect
from datetime import datetime
from Jagrati import settings
from django.conf.urls.static import static 

from django.contrib.auth.models import User
from accounts.models import Profile
from events.models import events

# Create your views here.
def index(request):
	data_old = events.objects.filter(date__lt = datetime.now())
	data_new = events.objects.filter(date__gte = datetime.now())
	
	context={'data_old': data_old, 'data_new':data_new}

	
	if request.user.is_authenticated:
		#if profile is completed, redirect to home page
		if Profile.objects.filter(user = request.user).exists():
			return render(request, "home/index.html", context)
		#else redirect to complete profile page
		else:
			return redirect('/accounts/create')
	else:
		return render(request, "home/index.html", context)

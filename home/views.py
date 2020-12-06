from django.shortcuts import render
from datetime import datetime
from Jagrati import settings

from django.conf.urls.static import static 

from events.models import events
# Create your views here.
def index(request):
	data_old = events.objects.filter(date__lt = datetime.now())
	data_new = events.objects.filter(date__gte = datetime.now())
	
	context={'data_old': data_old, 'data_new':data_new}
	return render(request, "home/index.html", context)

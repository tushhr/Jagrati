from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login as auth_login, logout
from django.contrib.auth.models import User

from .models import *
from accounts.models import Profile

# Create your views here.
#Home page

@login_required
def index(request):
	current_user = request.user
	#if profile is completed, redirect to inventory page	
	if Profile.objects.filter(user = current_user).exists():
		return render(request, 'inventory/home.html')
	#else redirect to complete profile
	else:
		return redirect('/accounts/create')

#when someone clicks on add item
def add_item(request):

	if request.method == "POST":
		asset_name=request.POST['asset_name']
		donated_by=request.POST['donated_by']
		quantity=request.POST['quantity']
		date=request.POST['date']

		#store transaction detail, with asset_name as lower to handle all case
		donation = asset_donation(asset_name=asset_name.lower(), donated_by=donated_by, quantity=quantity, date=date )
		#saving donation transaction
		donation.save()

		#all rows with asset name as given in the form
		item=asset.objects.filter(asset_name = asset_name.lower())

		#if the item already exits, increase its quantity, else create new row!
		if item.exists():
			new_item = asset.objects.get(asset_name = asset_name.lower())
			new_item.quantity = int(new_item.quantity) + int(quantity)
		else:
			new_item = asset(asset_name=asset_name.lower(), quantity = quantity)

		#saving item details
		new_item.save()
		messages.success(request, "Transaction Successfull!")

		#redirect to inventory page
		return redirect('/inventory')

@login_required
def withdraw(request):

	if request.method == "POST":
		asset_name=request.POST['asset_name']
		volunteer=request.POST['volunteer']
		quantity=request.POST['quantity']
		date=request.POST['date']

		#check the username
		current_user = request.user

		#if it won't match, cancel transaction
		if volunteer != current_user.username:
			messages.error(request, "Please login with same username, as you want the transaction to be placed.")
			return redirect('/inventory')
		else:

			#Check for valid item
			item=asset.objects.filter(asset_name = asset_name.lower())

			#if item exists
			if item.exists():
				remove_item = asset.objects.get(asset_name = asset_name.lower())
				#check for quantity, does we have given amount of quantity of that item
				if int(remove_item.quantity) >= int(quantity):
					#if yes, then subtract the number of quantity removed.
					remove_item.quantity = int(remove_item.quantity) - int(quantity)
					
					#saving withdrawn transaction details
					withdraw = asset_transaction(asset_name= asset_name.lower(), volunteer=volunteer, quantity=quantity, date=date )
					withdraw.save()
					
					#saving asset details
					remove_item.save()
					messages.success(request, "Transaction Successfull!")
					return redirect('/inventory')
				else:
					messages.error(request, "Sorry, we don't have much "+asset_name+" in our warehouse.")
					return redirect('/inventory')
			
			else:
				messages.error(request, "Invalid "+asset_name)
				return redirect('/inventory')
		
		
		return			
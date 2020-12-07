from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Profile

# Create your views here.
def index(request):

	#if user is logged in, redirect to home page
	if  request.user.is_authenticated:
		return redirect('/')
	#else redirect to login page
	else:
		return render(request, 'accounts/login.html')

def signup(request):
	
	if request.method == "POST":
		username=request.POST['username']
		email=request.POST['email']
		pass1=request.POST['pass1']
		pass2=request.POST['pass2']
		
		#to check user entered information
		#queryset of user based on, username and email
		user = User.objects.filter(username=username)
		user2 = User.objects.filter(email=email)

		#if same username exits
		if user.exists():
			messages.error(request, "Account with entered username already exists")
			return redirect('/accounts')
		
		#if same email address already exits
		if user2.exists():
			messages.error(request, "Account with entered email already exists")
			return redirect('/accounts')

		#if password won't match
		if (pass1!= pass2):
			messages.error(request, "Passwords do not match")
			return redirect('/accounts')

		# Create the user
		user = User.objects.create_user(username, email, pass1)
		user.set_password(pass1)
		user.save()

		
		return redirect('/')
		    
	else:
		return render(request, 'error.html')

def create(request):
	
	user = request.user

	if request.method == 'POST':
		roll_no = request.POST['roll_no']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		gender = request.POST['gender']
		batch = request.POST['batch']
		programme = request.POST['programme']
		dob = request.POST['dob']
		contact_no = request.POST['contact_no']
		alt_email = request.POST['alt_email']
		street_address1 = request.POST['street_address1']
		street_address2 = request.POST['street_address2']
		city = request.POST['city']
		state = request.POST['state']
		pincode = request.POST['pincode']

		profile = Profile(
		    user=user, first_name=first_name, last_name=last_name, roll_no=roll_no, dob=dob, batch=batch,
		    programme=programme, gender=gender, alt_email=alt_email,
		    contact_no=contact_no, street_address1=street_address1,
		    street_address2=street_address2, city=city, state=state,
		    pincode=pincode,
		)
		profile.save()

		return redirect('/')

	else:
		return render(request, 'accounts/create_profile.html')

def login(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        password=request.POST['password']


        user=authenticate(username = username, password = password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/accounts")

    return render(request, "error.html")


def logout(request):
	auth_logout(request)
	messages.success(request, "Successfully logged out")
	return redirect('/accounts')

	
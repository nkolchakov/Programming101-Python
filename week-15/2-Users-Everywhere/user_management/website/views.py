from django.shortcuts import render
from .models import User
# Create your views here.

def register(request):
	if request.method == 'POST':
		email = request.POST['username_email']
		password = request.POST['username_password']

		user = User(email=email, password = password )
		user.save()

	return render(request, 'register.html')

def login(request):

	email = request.POST['username_email']
	password = request.POST['username_password']

	return render(request, 'login.html')

def profile(request):
	return render(request, 'profile.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from hospital.models import *

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'Username or password do not exist')

    context = {}
    return render(request, 'hospital/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'hospital/home.html')

def appoinment(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/appointment.html', { 'doctors': doctors})

def profile(request):
    return render(request, 'hospital/profile.html');
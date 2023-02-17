from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Authentication views

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'})
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
        user.save()
        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'message': 'Invalid request'})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'User logged in successfully'})
        else:
            return JsonResponse({'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request'})

def logout_user(request):
    logout(request)
    return JsonResponse({'message': 'User logged out successfully'})
from django.shortcuts import render

def home(request):
    return render(request, 'login/home.html')

def login(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'login/register.html')
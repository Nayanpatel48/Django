from django.shortcuts import render

def home(request):
    return render(request, 'login/home.html')

def get_started(request):
    return render(request, 'login/get_started.html')
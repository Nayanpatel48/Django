from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "layout.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")

def shopping(request):
    return render(request, "website/shopping.html")
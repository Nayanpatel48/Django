from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")
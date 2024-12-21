from django.urls import path
# path is used to define url patterns

from . import views
# imported views, this views are classes or functions which handles the request for specific
# urls

urlpatterns = [
    path('', views.home, name='home'),
    # / (the root URL for this app)
    # This is the homepage for the app. When someone accesses the base URL of 
    # this app (e.g., http://127.0.0.1:8000/ if this app is directly included 
    # in the project), the home view function will handle the request.

    path('login/', views.login, name='login'),
    # This URL is for the login page of the application.
    # Example: Accessing http://127.0.0.1:8000/login/ will display the login form.
    
    path('register/', views.register, name='register'),
    # his URL is for the registration page where new users can sign up for the application.
    # Example: Accessing http://127.0.0.1:8000/register/ will display a registration form.
]
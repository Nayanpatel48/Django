from django.urls import path
# path is used to define url patterns

from . import views
# imported views, this views are classes or functions which handles the request for specific
# urls

urlpatterns = [
    path('', views.register, name='register'),
    # This URL is for the register page of the application.
    # Example: Accessing http://127.0.0.1:8000/register/ will display the register form.
    
    path('success/', views.success, name='success'),
    # this URL is for the registration success page.
    # Example: Accessing http://127.0.0.1:8000/success_page/ will display success page.

    path('user_list/', views.user_list, name='user_list'),
]
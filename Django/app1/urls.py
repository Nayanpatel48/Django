from django.urls import path
from .views import StudentFormHandlingView, StudentDetailsDisplayAndFetching

urlpatterns = [
    path('', StudentDetailsDisplayAndFetching.as_view(), name='student_list'),
    
    path('students/', StudentDetailsDisplayAndFetching.as_view(), name='student_list'),
    
    path('add_student/', StudentFormHandlingView.as_view(), name='add_student'),
    # .as_view() Converts the class into a callable view function that Django’s URL 
    # dispatcher can use.
]
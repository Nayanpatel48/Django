from django.shortcuts import render

from django.views.generic.edit import CreateView
# A built-in generic CBV in Django that simplifies the creation of new records in the database.
# It automatically handles form display, form validation, and saving the data to the database.

from .forms import InsertDataOfStudent

from django.views.generic.list import ListView
# ListView is a generic view provided by Django to handle displaying a list of objects 
# from the database.

from .models import Student

from django.urls import reverse_lazy
# It ensures the URL is resolved only when needed (e.g., when the view redirects).

class StudentFormHandlingView(CreateView):
    
    # this shows that this view is `associated`` with `Student` model
    model = Student
    
    form_class = InsertDataOfStudent
    # the `InsertDataOfStudent` is a form class used to render and validate the form.
    
    template_name = 'add_student.html'
    # this specifies the template used to render the form
    
# view for handling student details fetching data from `Student` model & displaying.
class StudentDetailsDisplayAndFetching(ListView):
    
    model = Student  # Specifies the model to fetch data from
    template_name = 'students.html'  # Template to render
    context_object_name = 'students'  # Name of the context variable passed to the template
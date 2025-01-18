# to view the model in your admin view you need to 'register your model' in this file.
from django.contrib import admin

# Register your models here.
# import model which you want to be displayed on your admin panel view
from .models import Student

# You can customize how the model is displayed in the Admin interface by using a ModelAdmin class.

class StudentViewOnAdminPanel(admin.ModelAdmin):
    # fields to display in your list view
    list_display = ('name','rollno','marks')

    # fieldss to be searchable in the admin table
    search_fields = ('rollno')
    
    # filter for listview
    list_filter = ('marks')

admin.site.register(Student)
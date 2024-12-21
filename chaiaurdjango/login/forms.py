# In Django forms are the frameworks for handling the user input, such as creating HTML forms
# ,validating input data and processing the input data in secure & clean manner.
# Djago forms simplify the process of rendering HTML forms, validating user data and integarating 
# form data with user input.

from django import forms
# django's forms module

from .models import UserProfile
# imported 'UserProfile' model from models to use it

class UserRegistrationForm(forms.ModelForm):
    # parameter forms.ModelForm automatically maps model fields to form fields.
    
    class Meta:
        model = UserProfile

        fields=['usename', 'email', 'phone_number', 'profile_image']
        # the list of fields from the model that should be included in the form.

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        # widgets customizes how the forms fields are rendered in HTML by specifying their attributes.
        # Here, fields are styled using css classes & placeholders.
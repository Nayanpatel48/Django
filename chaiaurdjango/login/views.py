from django.shortcuts import render, redirect
# here 'render' is used to render the HTML page along with context data
# here 'redirect' will redirect the user to the next page after successful operation.

from .forms import UserRegistrationForm
# A Django ModelForm imported from the forms.py file, which handles the user registration process.

from .models import UserProfile

def register(request):
    # This defines the register view function, which takes an HttpRequest object (request) as 
    # its argument.
    if request.method == 'POST':
        # POST: Indicates that the form has been submitted, and the data is available in 
        # request.POST and request.FILES.

        form = UserRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            # Checks if the submitted data meets the validation criteria defined in the 
            # UserRegistrationForm and the underlying model (UserProfile).

            form.save()
            # Saves the valid form data to the database.

            return redirect('success')
            # Redirects the user to a success page (e.g., a "Registration Successful" page) 
            # after the form is successfully saved.
    else:
        form = UserRegistrationForm()
        # An empty form is created for display when the user visits the registration page.

    return render(request, 'register.html', {'form': form})
    #Renders the register.html template with the form context variable.
    #If the form is empty (GET request) or contains invalid data (POST 
    # request), it is passed back to the template for display.

def success(request):
    return render(request, 'success.html')

def user_list(request):
    users = UserProfile.objects.all()
    # UserProfile.objects.all() is a Django ORM query that retrieves all 
    # records from the UserProfile table in the database.

    return render(request, 'user_list.html', {'users': users})
# this function retrieves all the UserProfile objects from the database & render 
# them in the HTML template

from django import forms
from .models import Student

# here InsertDataOfStudent is a subclass of forms.ModelForm:
class InsertDataOfStudent(forms.ModelForm):
    #  It is a special class inside a ModelForm that provides metadata about 
    # the model and how the form should behave.
    class Meta:
        
        # this line shows that this form is associated with 'Student' model
        model = Student
        
        # This line tells Django which fields from the 'Student' model should be included in the form.
        fields=['name', 'rollno', 'marks']
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)
    
    # special method in python which defines the string representation of object
    def __str__(self):
        return self.name
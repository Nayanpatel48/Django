from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# first model named ChaiVariety
class ChaiVariety(models.Model):
    # enums
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('EL', 'ELICHI')
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# one to many
class ChaiReview(models.Model):
    chai=models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    data_added = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'

# many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    # many to many
    chai_varieties=models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name
    
# one to one 
class ChaiCertificate(models.Model):
    # one to one
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')

    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'

        
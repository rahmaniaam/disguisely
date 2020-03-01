from django.db import models

# Create your models here.

class Disguise(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    dob = models.DateField()
    img = models.CharField(max_length=250)
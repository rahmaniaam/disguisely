from django.db import models
# Create your models here.

class Disguise(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    city = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    dob = models.DateField(null=True)
    img = models.ImageField(upload_to='images/')

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
from django.db import models

class Promoter(models.Model):    
    
    address = models.CharField(max_length=100)
    cell_phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    comments = models.CharField(max_length=500)
    company = models.CharField(max_length=100)
    email = models.CharField(max_length=75)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
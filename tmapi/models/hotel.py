from django.db import models

class Hotel(models.Model):

    address = models.CharField(max_length=200)
    confirmation = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    phone = models.CharField(max_length=30)
    
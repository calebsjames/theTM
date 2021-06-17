from django.db import models

class Venue(models.Model):

    address = models.CharField(max_length=100)
    capacity = models.IntegerField()
    cell = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    hall_fee = models.IntegerField()
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    merch_sales = models.CharField(max_length=100)
    merch_fee = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=15)
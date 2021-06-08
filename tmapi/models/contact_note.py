from django.db import models

class ContactNote(models.Model):

    date = models.DateField()
    text = models.CharField(max_length=200)
    method = models.CharField(max_length=20)
    venue = models.ForeignKey("Venue", on_delete=models.CASCADE)

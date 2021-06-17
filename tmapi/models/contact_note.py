from django.db import models

class ContactNote(models.Model):

    date = models.DateField()
    text = models.CharField(max_length=200)
    method = models.CharField(max_length=20)
    show = models.ForeignKey("Show", on_delete=models.CASCADE)

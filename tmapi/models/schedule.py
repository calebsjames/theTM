from django.db import models

class Schedule(models.Model):        
    
    date = models.DateField()
    description = models.CharField(max_length=200)
    show = models.ForeignKey("Show", on_delete=models.CASCADE)
    time = models.TimeField()
from django.db import models
from datetime import date, time 

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, 
        related_name="category",
        
        )
    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    event= models.ManyToManyField(Event, related_name="event") 
    def __str__(self):
        return self.name




from django.db import models
from datetime import date, time 
from django.db.models.signals import post_save,pre_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
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
    location = models.CharField(max_length=250)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, 
        related_name="category",
        
        )
    participants = models.ManyToManyField(User, related_name="rsvp_events", blank=True)
    asset = models.ImageField(upload_to='events-asset',blank=True,null=True)


    def __str__(self):
        return self.name
    
class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rsvps')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    is_active = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.user.username} - {self.event.name}"




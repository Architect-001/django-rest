from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)

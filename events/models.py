from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_online = models.BooleanField(default=False)
    max_seats = models.PositiveIntegerField()
    booking_open_window_start = models.DateTimeField()
    booking_open_window_end = models.DateTimeField()

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

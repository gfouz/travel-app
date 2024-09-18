from django.db import models
from tickets.models import Ticket

class Passenger(models.Model):
    role = models.CharField(max_length=255, default='Pasajeros')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    passport = models.CharField(max_length=50)
    # email = models.EmailField(unique=True, null=True, blank=True)
    ticket = models.ForeignKey(Ticket,null=True, blank=True, on_delete=models.CASCADE, related_name='passengers')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

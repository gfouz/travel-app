from django.db import models
from tickets.models import Ticket

class CheckIn(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    passport = models.CharField(max_length=50)
    reservation_code = models.CharField(max_length=50)
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    attached_document = models.FileField(upload_to='documents/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

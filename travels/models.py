from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User



class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]
    
    cover_photo = models.ImageField(upload_to='covers/')
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    destination = models.CharField(max_length=255)
    airline = models.CharField(max_length=255)
    departure_datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CheckIn(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    
    full_name = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    passport_number = models.CharField(max_length=20)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    departure_datetime = models.DateTimeField()
    attachment = models.FileField(upload_to='attachments/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Settings(models.Model):
    whatsapp = models.CharField(max_length=20)

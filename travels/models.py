from datetime import timezone
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore


class Ticket(models.Model):
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True)
    name = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    airline = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    last_reservation_deadline = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def update_status(self):
        now = timezone.now()

        if self.last_reservation_deadline < now:
            self.status = self.StatusChoices.UNAVAILABLE
        elif self.departure_date - timezone.timedelta(days=1) <= now:
            self.status = self.StatusChoices.AVAILABLE
        else:
            self.status = self.StatusChoices.DRAFT
        
        self.save()

    def __str__(self):
        return f"{self.price} - {self.airline} ({self.status})"

class Flight(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=255)
    date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    luggage = models.IntegerField()  # Suponiendo que es un número

class CheckIn(models.Model):
    fullname = models.CharField(max_length=255)
    passport = models.CharField(max_length=50)
    ticket_number = models.CharField(max_length=50)
    reservation_code = models.CharField(max_length=50)
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=255)
    attached_document = models.FileField(upload_to='documents/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Adjustment(models.Model):
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

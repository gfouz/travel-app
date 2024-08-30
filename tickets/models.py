import pendulum
# from datetime import timezone
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from flights.models import Flight

class Ticket(models.Model):
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True, null=True)
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    airline = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    last_reservation_date = models.DateTimeField()
    flights = models.ForeignKey(Flight, on_delete=models.PROTECT)
    ticket_issuer = models.ForeignKey(User, on_delete=models.PROTECT)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def update_status(self, span=7):
        now = pendulum.now()  # Get the current date and time using pendulum

        # Convert last_reservation_date to a pendulum instance
        last_reservation = pendulum.instance(self.last_reservation_date)

        if last_reservation.is_past():
            self.status = 'unavailable'  # Set status to unavailable if the date has passed
        elif last_reservation.subtract(days=span) <= now:
            self.status = 'available'  # Set status to available if the date is within the 7 next day
        else:
            self.status = 'draft'  # Otherwise, set status to draft
        
        self.save()

    def __str__(self):
        return f"{self.price} - {self.airline} ({self.status})"
        



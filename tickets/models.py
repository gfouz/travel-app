#import pendulum
# from datetime import timezone
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from flights.models import Flight # type: ignore

class Ticket(models.Model):
    role = models.CharField(max_length=255, default='Pasajes')
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True, null=True)
    STATUS_CHOICES = [
        ('reserved', 'Reserved'),
        ('expired', 'Expired'),
    ]
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='', null=True, blank=True)
    passport = models.CharField(max_length=40, default='')
    checked= models.BooleanField(default=False)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='scheduled')
    booking_code = models.CharField(max_length=255)
    adult_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    child_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    infant_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets')
    ticket_issuer = models.ForeignKey(User, on_delete=models.PROTECT)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #last_reservation_date = models.DateTimeField()
    """
    def update_status(self):
        now = pendulum.now()  # Get the current date and time using pendulum

        # Convert last_reservation_date to a pendulum instance
        last_reservation = pendulum.instance(self.last_reservation_date)

        if last_reservation.is_past():
            self.status = 'expired'  # Set status to unavailable if the date has passed
        #elif last_reservation.subtract(days=span) <= now:
            #self.status = 'available'  # Set status to available if the date is within the 7 next day
        #else:
            #self.status = 'draft'  # Otherwise, set status to draft
    self.save()

    def __str__(self):
        return f"{self.booking_code}"
    """    


from django.db import models
import pendulum

class Flight(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('expired', 'Expired'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    isMain= models.BooleanField(default=False)
    isConnected = models.BooleanField(default=False)
    role= models.CharField(max_length=255, default='Vuelos')
    departure_place = models.CharField(max_length=255)
    arrival_place = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=255)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    departure_date= models.DateTimeField()
    adult_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    child_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    infant_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    luggage = models.IntegerField( blank=True, null=True) 
    connection_flight = models.ForeignKey( 'self', on_delete=models.CASCADE, null=True, related_name='connected_flight')

    def update_status(self, span=30):
        now = pendulum.now()  # Get the current date and time using pendulum

        # Convert last_reservation_date to a pendulum instance
        departure_date = pendulum.instance(self.departure_date)

        if departure_date.is_past():
            self.status = 'expired'  # Set status to unavailable if the date has passed
        elif departure_date.subtract(days=span) <= now:
            self.status = 'available'  # Set status to available if the date is within the 7 next day
        else:
            self.status = 'draft'  # Otherwise, set status to draft
        self.save()

    def __str__(self):
        return f"{self.role} - {self.flight_number} ({self.status})"

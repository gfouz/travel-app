from django.db import models
import pendulum

class Flight(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('available', 'Available'),
        ('expired', 'Expired'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='scheduled')
    isMain= models.BooleanField(default=False)
    isConnected = models.BooleanField(default=False)
    role= models.CharField(max_length=255, default='Vuelos')
    departure_place = models.CharField(max_length=255)
    arrival_place = models.CharField(max_length=255)
    airline = models.CharField(max_length=255, null=True, blank=True )
    flight_number = models.CharField(max_length=255, null=True, blank=True )
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    departure_date= models.DateField()
    adult_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    child_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    infant_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    luggage = models.IntegerField( blank=True, null=True) 
    connection_flight = models.ForeignKey( 'self', on_delete=models.CASCADE, null=True, related_name='connected_flight')

    def update_status(self, unavailable_days=3, available_days=10):
        now = pendulum.now()
        departure = pendulum.instance(self.departure_date)

        # Calcula las fechas límite
        unavailable_days_before = departure.subtract(days=unavailable_days)
        available_days_before = departure.subtract(days=available_days)
        
        old_status = self.status

        # Expired if the current date is after the departure date
        if now.date() > departure:
            self.status = 'expired'
    
        # Unavailable if the flight is within 3 days before the departure date
        elif now.date() >= unavailable_days_before:
            self.status = 'unavailable'
    
        # Available if the flight is within 7 days but more than 3 days away
        elif now.date() >= available_days_before:
            self.status = 'available'
    
        # Scheduled if the flight is more than 7 days away
        else:
            self.status = 'scheduled'

        # Only save the updated status if it has changed
        if old_status != self.status:
            self.save()

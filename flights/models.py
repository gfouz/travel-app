from django.db import models
from tickets.models import Ticket  # type: ignore


class Flight(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=255)
    date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    luggage = models.IntegerField( blank=True, null=True)  # Suponiendo que es un número

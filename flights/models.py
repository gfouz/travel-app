from django.db import models


class Flight(models.Model):
    role= models.CharField(max_length=255, default='Vuelos')
    departure_place = models.CharField(max_length=255)
    arrival_place = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=255)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    departure_date= models.DateField()
    luggage = models.IntegerField( blank=True, null=True)  # Suponiendo que es un número

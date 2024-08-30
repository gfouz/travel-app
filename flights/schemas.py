from ninja import ModelSchema, Schema
from datetime import time, date
from flights.models import Flight

class FlightSchema(ModelSchema):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightCreateSchema(Schema):
    flight_number: str
    departure_place: str 
    arrival_place: str
    departure_time: time
    arrival_time: time
    departure_date: date
    luggage: int 

class FlightUpdateSchema(Schema):
    flight_number: str
    departure_place: str 
    arrival_place: str
    departure_time: time
    arrival_time: time
    departure_date: date
    luggage: int 

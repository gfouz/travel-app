from ninja import ModelSchema, Schema
from datetime import time, date
from .models import Flight
from typing import List


class TicketSchema(Schema):
    id: int
    price: float
    status: str
    airline: str
    booking_code: str
    description: str


class FlightSchema(ModelSchema):
    tickets: List[TicketSchema]
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


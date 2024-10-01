from ninja import ModelSchema, Schema
from datetime import time, date
from .models import Flight
from typing import List

class DeleteMessageSchema(Schema):
    message: str


class TicketSchema(Schema):
    id: int
    checked: bool
    status: str
    infant_price: float
    child_price: float
    adult_price: float
    booking_code: str
    
class ConnectionFlightSchema(Schema):
    flight_number: str
    status: str
    departure_place: str 
    arrival_place: str
    departure_time: time
    arrival_time: time
    departure_date: date
    adult_price: float 
    child_price: float
    infant_price: float
    luggage: int 
      
class FlightSchema(ModelSchema):
    tickets: List[TicketSchema]
    connected_flight: List[ConnectionFlightSchema]
    class Meta:
        model = Flight
        fields = '__all__'
        

class FlightCreateSchema(Schema):
    airline: str=None
    flight_number: str
    departure_place: str 
    arrival_place: str
    departure_time: time
    arrival_time: time
    departure_date: date
    adult_price: float
    child_price: float
    infant_price: float
    luggage: int 
    connection_flight_id: int=None

class FlightUpdateSchema(Schema):
    airline: str=None
    flight_number: str
    departure_place: str 
    arrival_place: str
    departure_time: time
    arrival_time: time
    departure_date: date
    adult_price: float 
    child_price: float
    infant_price: float
    luggage: int 


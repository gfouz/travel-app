from ninja import ModelSchema, Schema
from flights.schemas import FlightSchema

from tickets.models import Ticket
from users.schemas import UserSchema
from typing import List

#from django.contrib.auth.models import User

class ErrorMessage(Schema):
    message: str

class DeleteMessage(Schema):
    message: str

    # exclude = ["last_login", "user_permissions"]
class AnyPassengerSchema(Schema):
    first_name: str
    last_name: str
    passport: str
        
class TicketSchema(ModelSchema):
    ticket_issuer: UserSchema
    flight: FlightSchema
    passenger: AnyPassengerSchema = None #Be sure to set this value to None to avoid validation errors.
    
    class Meta:
        model = Ticket
        fields = '__all__'
 

class TicketCreateSchema(Schema):
    airline: str
    adult_price: float 
    child_price: float
    infant_price: float
    description: str
    ticket_issuer_id: int=None # similar to user_id
    flight_id: int=None # the flight for this ticket
    booking_code: str
    last_reservation_date: str
    

class TicketUpdateSchema(Schema):
    airline: str
    adult_price: float 
    child_price: float
    infant_price: float
    description: str
    ticket_issuer_id: int=None #similar to user_id
    flight_id: int=None #the flight for this ticket
    booking_code: str
    last_reservation_date: str


   

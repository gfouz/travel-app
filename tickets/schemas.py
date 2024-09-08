from ninja import ModelSchema, Schema
from tickets.models import Ticket
from flights.schemas import FlightSchema



from django.contrib.auth.models import User
from datetime import datetime


class ErrorMessage(Schema):
    message: str


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "username"]

    # exclude = ["last_login", "user_permissions"]

        
class TicketSchema(ModelSchema):
    ticket_issuer: UserSchema
    flights: FlightSchema
    
    class Meta:
        model = Ticket
        fields = ['id', 'status', 'airline', 'price','flights', 'description', 'last_reservation_date', 'ticket_issuer']


class TicketCreateSchema(Schema):
    airline: str
    price: float
    description: str
    ticket_issuer_id: int=None # similar to user_id
    flight_id: int=None # the flight for this ticket
    last_reservation_date: str
    

class TicketUpdateSchema(Schema):
    airline: str
    price: float
    description: str
    ticket_issuer_id: int=None #similar to user_id
    flight_id: int=None #the flight for this ticket
    last_reservation_date: str


   

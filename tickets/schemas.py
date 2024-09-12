from ninja import ModelSchema, Schema
from flights.schemas import FlightSchema
from tickets.models import Ticket
from users.schemas import UserSchema
#from django.contrib.auth.models import User


class ErrorMessage(Schema):
    message: str


    # exclude = ["last_login", "user_permissions"]
class CheckinSchema(Schema):
    passport: str
        
class TicketSchema(ModelSchema):
    ticket_issuer: UserSchema
    flight: FlightSchema
    
    class Meta:
        model = Ticket
        fields = '__all__'
 

class TicketCreateSchema(Schema):
    airline: str
    price: float
    description: str
    ticket_issuer_id: int=None # similar to user_id
    flight_id: int=None # the flight for this ticket
    booking_code: str
    last_reservation_date: str
    

class TicketUpdateSchema(Schema):
    airline: str
    price: float
    description: str
    ticket_issuer_id: int=None #similar to user_id
    flight_id: int=None #the flight for this ticket
    booking_code: str
    last_reservation_date: str


   

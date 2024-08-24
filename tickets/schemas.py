from ninja import ModelSchema, Schema
from tickets.models import Ticket
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
    
    class Meta:
        model = Ticket
        fields = ['id', 'status', 'airline', 'price', 'description', 'created_at', 'ticket_issuer']


class TicketCreateSchema(Schema):
    airline: str
    price: float
    description: str
    ticket_issuer_id: int=None # similar to user_id
    last_reservation_date: datetime
    

class TicketUpdateSchema(Schema):
    name: str
    airline: str
    price: float
    description: str
    ticket_issuer_id: int=None # similar to user_id
    last_reservation_date: datetime



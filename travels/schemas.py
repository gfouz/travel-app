from ninja import ModelSchema, Schema
from travels.models import Ticket, CheckIn, Adjustment, Flight
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

class CheckInSchema(ModelSchema):
    class Meta:
        model = CheckIn
        fields = '__all__'  # Include all fields

class FlightSchema(ModelSchema):
    class Meta:
        model = Flight
        fields = '__all__'

class AdjustmentSchema(ModelSchema):
    class Meta:
        model = Adjustment
        fields = '__all__'  # Include all fields

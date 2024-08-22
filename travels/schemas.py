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
    created_by: UserSchema
    
    class Meta:
        model = Ticket
        fields = ['id', 'cover_photo', 'status', 'airline', 'price', 'description', 'created_at', 'created_by']


class TicketCreateSchema(ModelSchema):
    class Meta:
        model = Ticket
        fields = ['cover_photo', 'airline', 'price', 'description', 'created_by']

class TicketUpdateSchema(ModelSchema):
    class Meta:
        model = Ticket
        fields = ['cover_photo', 'status', 'airline', 'price', 'description']

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

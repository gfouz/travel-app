from ninja import ModelSchema, Schema
from travels.models import Ticket, CheckIn, Settings
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
    user: UserSchema
    
    class Meta:
        model = Ticket
        fields = '__all__'  # Include all fields


class CheckInSchema(ModelSchema):
    class Meta:
        model = CheckIn
        fields = '__all__'  # Include all fields

class SettingsSchema(ModelSchema):
    class Meta:
        model = Settings
        fields = '__all__'  # Include all fields

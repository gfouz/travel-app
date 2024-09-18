from ninja import ModelSchema, Schema
from tickets.schemas import TicketSchema
from .models import Passenger


class DeleteMessageSchema(Schema):
    message: str


class PassengerSchema(ModelSchema):
    ticket: TicketSchema
    class Meta:
        model = Passenger
        fields = '__all__'  # This will include all fields in the schema

class CreatePassengerSchema(Schema):
    first_name: str
    last_name: str
    passport: str
    ticket_id: int = None  # Debe ser el ID del ticket relacionado

class UpdatePassengerSchema(Schema):
    first_name: str
    last_name: str
    passport: str
    # ticket_id no se incluye aquí para permitir la actualización sin modificar la relación


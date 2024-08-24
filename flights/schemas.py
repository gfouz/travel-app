from ninja import ModelSchema, Schema
from datetime import datetime




class FlightSchema(ModelSchema):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightCreateSchema(Schema):
    flight_number: str
    ticket_id: int=None
    from_location: str 
    to_location: str
    date: datetime

class FlightUpdateSchema(Schema):
    flight_number: str
    ticket_id: int=None
    from_location: str 
    to_location: str
    date: datetime

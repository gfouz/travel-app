from ninja import ModelSchema, Schema
from tickets.schemas import TicketSchema
from checkins.models import CheckIn


class CheckInSchema(ModelSchema):
    ticket: TicketSchema
    
    class Meta:
        model = CheckIn
        fields = '__all__'  # Include all fields
        
class CheckInCreateSchema(Schema):
    first_name: str
    last_name: str
    passport: str
    booking_code: str
    ticket_id: int=None
    

class CheckInUpdateSchema(Schema):
    first_name: str
    last_name: str
    passport: str
    booking_code: str  

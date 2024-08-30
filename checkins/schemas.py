from ninja import ModelSchema, Schema
from tickets.schemas import TicketSchema
from checkins.models import CheckIn


class CheckInSchema(ModelSchema):
    ticket: TicketSchema
    
    class Meta:
        model = CheckIn
        fields = '__all__'  # Include all fields
        
class CheckInCreateSchema(Schema):
    fullname: str
    passport: str
    ticket_number: str
    reservation_code: str
    ticket_id: int=None
    

class CheckInUpdateSchema(Schema):
    fullname: str
    passport: str     

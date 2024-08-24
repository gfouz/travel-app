from ninja import ModelSchema, Schema


class CheckInSchema(ModelSchema):
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

from ninja import ModelSchema, Schema
from adjustments.models import Setting

class DeleteMessage(Schema):
    message: str

class SettingSchema(ModelSchema):
    class Meta:
        model = Setting
        fields = '__all__'

class SettingCreateSchema(Schema):
    email: str 
    whatsapp: str
    available_days: int
    unavailable_days: int
    
class SettingUpdateSchema(Schema):
    email: str 
    whatsapp: str
    available_days: int
    unavailable_days: int
    

from ninja import ModelSchema, Schema
from adjustments.models import Adjustment

class AdjustmentSchema(ModelSchema):
    class Meta:
        model = Adjustment
        fields = '__all__'

class AdjustmentCreateSchema(Schema):
    email: str 
    whatsapp: str
    

class AdjustmentUpdateSchema(Schema):
    email: str 
    whatsapp: str
    

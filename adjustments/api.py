from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from adjustments.models import Adjustment
from adjustments.schemas import AdjustmentSchema, AdjustmentCreateSchema, AdjustmentUpdateSchema

from core.api import Router


router = Router()

@router.post("/createAdjustment", response={ 200: AdjustmentSchema })
def create_adjustment(request, payload: AdjustmentCreateSchema ):
    adjustment = Adjustment.objects.create(**payload.dict())
    return adjustment

    
@router.get("/getAdjustment/{adjustment_id}", response={ 200: AdjustmentSchema })
def get_adjustment(request, adjustment_id: int):
    adjustment = get_object_or_404(Adjustment, id=adjustment_id)
    return adjustment  

    
@router.get("/getAdjustments", response=List[AdjustmentSchema])
def list_adjustment(request):
    adjustments = Adjustment.objects.all()
    return adjustments  

@router.put("/updateAdjustment/{adjustment_id}", response={ 200: AdjustmentSchema })
def update_adjustment(request, adjustment_id: int, payload: AdjustmentUpdateSchema ):
    adjustment = get_object_or_404(Adjustment, id=adjustment_id)
    for attr, value in payload.dict().items():
        setattr(adjustment, attr, value)
    adjustment.save()
    return adjustment


@router.delete("/deleteAdjustment/{adjustment_id}")
def delete_adjustment(request, adjustment_id: int):
    adjustment = get_object_or_404(Adjustment, id=adjustment_id)
    adjustment.delete()
    return {"message": "Adjustment deleted successfully"}

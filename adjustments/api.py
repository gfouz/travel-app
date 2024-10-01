from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from adjustments.models import Setting
from adjustments.schemas import SettingSchema, SettingCreateSchema, SettingUpdateSchema, DeleteMessage
from ninja import Router

router = Router()

    
@router.post("/create-setting", response={ 200: SettingSchema })
def create_setting(request, payload: SettingCreateSchema):
    if Setting.objects.exists():
        raise HttpError(400, "A Setting instance already exists.")
    setting = Setting(**payload.dict())
    setting.save()
    return setting


    
@router.get("/get-setting/{setting_id}", response={ 200: SettingSchema })
def get_setting(request, setting_id: int):
    setting = get_object_or_404(Adjustment, id=setting_id)
    return setting  

    
@router.get("/get-setting", response={ 200: SettingSchema })
def get_setting(request):
    setting = get_object_or_404(Setting)
    return setting

@router.put("/update-setting/{setting_id}", response={ 200: SettingSchema })
def update_setting(request, setting_id: int, payload: SettingUpdateSchema ):
    setting = get_object_or_404(Setting, id=setting_id)
    for attr, value in payload.dict().items():
        setattr(setting, attr, value)
    setting.save()
    return setting


@router.delete("/delete-setting/{setting_id}", response={200:DeleteMessage})
def delete_setting(request, setting_id: int):
    setting = get_object_or_404(Setting, id=setting_id)
    setting.delete()
    return 200, {"message": "Success,Ticket was deleted!"}



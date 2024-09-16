
from typing import List
from django.http import HttpResponse, Http404
from ninja.errors import HttpError
from .models import CheckIn, Ticket
from .schemas import CheckInSchema, CheckInCreateSchema, CheckInUpdateSchema, DeleteMessageSchema
#from core.api import router
from ninja import Router
router = Router()

@router.post('/create-checkin', response={200: CheckInSchema})
def create_checkin(request, payload: CheckInCreateSchema):
    """Create a new checkin"""
    try:
        ticket = Ticket.objects.get(id=payload.ticket_id)
        checkin = CheckIn.objects.create(ticket=ticket, **payload.dict(exclude={'ticket_id'}))
        return checkin
    except Ticket.DoesNotExist:
        raise HttpError(404, "Ticket not found")
    except Exception as e:
        raise HttpError(500, detail=str(e))

@router.get('/get-checkins', response={200: List[CheckInSchema] })
def get_checkins(request):
    """Get all checkins"""
    checkins = CheckIn.objects.all()
    return checkins

@router.get('/get-checkin/{checkin_id}', response={200: CheckInSchema})
def get_checkin(request, checkin_id: int):
    """Get a checkin by id"""
    checkin= get_object_or_404(CheckIn, id=checkin_id)
    return checkin

@router.put('/update-checkin/{checkin_id}')
def update_checkin(request, checkin_id: int, payload: CheckInUpdateSchema):
    """Update a checkin"""
    try:
        checkin = get_object_or_404(CheckIn, id=checkin_id)
        checkin.first_name = payload.first_name
        checkin.last_name = payload.last_name
        checkin.passport = payload.passport
        checkin.booking_code = payload.booking_code
        checkin.save()
        return checkin
    except CheckIn.DoesNotExist:
        raise HttpError(404, "Ticket not found")

@router.delete("/delete-checkin/{checkin_id}", response={200: DeleteMessageSchema})
def delete_checkin(request, checkin_id: int):
    checkin = get_object_or_404(CheckIn, id=checkin_id)
    checkin.delete()
    return 200, {"message": "Success,Ticket was deleted!"}

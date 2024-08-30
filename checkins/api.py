"""
checkin_api.py


This module defines the API for managing check-ins in the system using Django Ninja.
It provides endpoints for creating, retrieving, and updating check-in records associated with tickets.

Endpoints:
- POST /checkins: Create a new check-in record.
- GET /checkins: Retrieve a list of all check-in records.
- GET /checkins/{id}: Retrieve a specific check-in record by its ID.
- PUT /checkins/{id}: Update an existing check-in record by its ID.

Schemas:
- CheckInCreateSchema: Schema for validating data when creating a new check-in.
- CheckInUpdateSchema: Schema for validating data when updating an existing check-in.
- CheckInSchema: Schema for serializing check-in data.

Models:
- CheckIn: The model representing a check-in record.
- Ticket: The model representing a ticket associated with check-ins.

Error Handling:
- Returns a 404 Not Found error if a check-in with a specified ID does not exist.

Example Usage:
- To create a new check-in, send a POST request to /checkins with the required fields.
- To retrieve all check-ins, send a GET request to /checkins.
- To retrieve a specific check-in, send a GET request to /checkins/{id} where {id} is the ID of the check-in.
- To update an existing check-in, send a PUT request to /checkins/{id} with the fields to be updated.

This module is designed to provide a simple interface for managing check-in records in a ticketing system, ensuring data integrity and ease of use.
"""



from django.http import HttpResponse, Http404
from ninja import Router
from ninja.errors import HttpError
from .models import CheckIn, Ticket
from .schemas import CheckInSchema, CheckInCreateSchema, CheckInUpdateSchema

router = Router()

@router.post('/create-checkin')
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

@router.get('/get-checkins')
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
        checkin.fullname = payload.fullname
        checkin.passport = payload.passport
        checkin.save()
        return checkin
    except CheckIn.DoesNotExist:
        raise HttpError(404, "Ticket not found")

@router.delete("/delete-checkin/{checkin_id}", response={204: None})
def delete_checkin(request, checkin_id: int):
    checkin = get_object_or_404(CheckIn, id=checkin_id)
    checkin.delete()
    return 204, None

"""
This module difines API endpoints for the Django Ninja endpoints.
It includes routes for handling HTTP request related to user operations
Descripción de los Endpoints
GET /api/tickets: Lista todos los tickets.
GET /api/tickets/{ticket_id}: Obtiene los detalles de un ticket específico por su ID.
POST /api/tickets: Crea un nuevo ticket. Requiere los datos definidos en TicketCreateSchema.
PUT /api/tickets/{ticket_id}: Actualiza un ticket existente. Solo actualiza los campos enviados en la solicitud (los no enviados permanecen iguales).
DELETE /api/tickets/{ticket_id}: Elimina un ticket específico por su ID.

"""

from ninja.security import HttpBearer
from django.conf import settings
from ninja import Router
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Ticket
from .schemas import TicketSchema, TicketCreateSchema, TicketUpdateSchema

import jwt

from ninja.errors import HttpError
from flights.models import Flight

router = Router()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            # print("this is the token :" + token)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload
        except:
            raise HttpError(401, "Not authorized, invalid token!")


@router.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"payload": request.auth}

    

@router.post("/create-ticket", response=TicketSchema)
def create_ticket(request, payload: TicketCreateSchema):
    user = User.objects.filter(pk=payload.ticket_issuer_id).first()
    if not user:
        raise HttpError(404, "User not found!")

    flight = Flight.objects.filter(pk=payload.flight_id).first()
    if not flight:
        raise HttpError(404, "Flight not found!")

    # Here you can add additional validation for last_reservation_date if needed
    if payload.last_reservation_date < pendulum.now().to_datetime_string():
        raise HttpError(400, "Last reservation date cannot be in the past!")

    ticket = Ticket.objects.create(
        ticket_issuer=user,
        flight=flight,
        airline=payload.airline,
        price=payload.price,
        description=payload.description,
        last_reservation_date=payload.last_reservation_date
    )
    
    ticket.update_status()
    return ticket

@router.get("/get-tickets", response=list[TicketSchema])
def list_tickets(request):
    return Ticket.objects.all()

@router.get("/get-ticket/{ticket_id}", response=TicketSchema)
def get_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return ticket


@router.put("/update-ticket/{ticket_id}", response=TicketSchema)
def update_ticket(request, ticket_id: int, data: TicketUpdateSchema):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(ticket, attr, value)
    ticket.update_status()  # Actualizar el estado del ticket si es necesario
    ticket.save()
    return ticket

@router.delete("/delete-ticket/{ticket_id}", response={204: None})
def delete_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return 204, None





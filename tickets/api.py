from ninja.security import HttpBearer
from django.conf import settings

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .schemas import TicketSchema, TicketCreateSchema, TicketUpdateSchema, DeleteMessage

import jwt
import pendulum
from ninja.errors import HttpError
from flights.models import Flight
from .models import Ticket
#from core.api import router
from ninja import Router
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
    if pendulum.parse(payload.last_reservation_date) < pendulum.now():
        raise HttpError(400, "Last reservation date cannot be in the past!")

    ticket = Ticket.objects.create(
        ticket_issuer=user,
        flight=flight,
        airline=payload.airline,
        booking_code = payload.booking_code,
        price=payload.price,
        description=payload.description,
        last_reservation_date=pendulum.parse(payload.last_reservation_date),
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
def update_ticket(request, ticket_id: int, payload: TicketUpdateSchema):
    # Obtener el ticket basado en el ID proporcionado
    ticket = Ticket.objects.filter(pk=ticket_id).first()
    if not ticket:
        raise HttpError(404, "User not found!")
    user = get_object_or_404(User, id=payload.ticket_issuer_id)
    flight = get_object_or_404(Flight, id=payload.flight_id)

    # Validar fecha de última reserva si se pasa en el payload
    if (
        payload.last_reservation_date
        and pendulum.parse(payload.last_reservation_date) < pendulum.now()
    ):
        raise HttpError(400, "Last reservation date cannot be in the past!")

    # Actualizar los campos del ticket según lo que se haya proporcionado en el payload
    if payload.ticket_issuer_id:
        ticket.ticket_issuer = user
    if payload.flight_id:
        ticket.flight = flight
    if payload.airline:
        ticket.airline = payload.airline
    if payload.booking_code:
        ticket.booking_code = payload.booking_code    
    if (
        payload.price is not None
    ):  # Se asume que el precio puede ser 0, así que lo comprobamos con is not None
        ticket.price = payload.price
    if payload.description:
        ticket.description = payload.description
    if payload.last_reservation_date:
        ticket.last_reservation_date = pendulum.parse(payload.last_reservation_date)

    # Guardar los cambios en el ticket
    ticket.save()

    # Actualizar el estado del ticket si es necesario
    ticket.update_status()

    return ticket


@router.delete("/delete-ticket/{ticket_id}", response={200:DeleteMessage})
def delete_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return 200, {"message": "Success,Ticket was deleted!"}


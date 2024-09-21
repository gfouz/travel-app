from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from tickets.models import Ticket
from .models import Passenger
from .schemas import PassengerSchema, CreatePassengerSchema, UpdatePassengerSchema, DeleteMessageSchema

#from core.api import router
from ninja import Router


router = Router()

@router.post("/create-passenger", response={ 200: PassengerSchema})
def create_passenger(request, payload: CreatePassengerSchema):
    # Asegurar que el ticket exista en la base de datos
    ticket_instance = get_object_or_404( Ticket, id=payload.ticket_id )

    if ticket_instance.status == 'booked':
        return {"error": "Ticket already reserved"}

    ticket_instance.status = 'booked'
    ticket_instance.save()
    
    # Crear el pasajero con la referencia al ticket
    passenger = Passenger.objects.create(
        **payload.dict( exclude={'ticket_id'} ),
          ticket=ticket_instance
    )
    return passenger

    
@router.get("/get-passenger/{passenger_id}", response={ 200: PassengerSchema })
def get_passenger(request, passenger_id: int):
    passenger = get_object_or_404(Passenger, id=passenger_id)
    return passenger  

    
@router.get("/get-passengers", response=List[PassengerSchema])
def list_flights(request):
    passengers = Passenger.objects.all()
    return passengers

@router.put("/update-passenger/{passenger_id}", response={ 200: UpdatePassengerSchema })
def update_flight(request, passenger_id: int, payload: UpdatePassengerSchema ):
    passenger = get_object_or_404(Passenger, id=passenger_id)
    for attr, value in payload.dict().items():
        setattr( passenger, attr, value)
    passenger.save()
    return passenger


@router.delete("/delete-passenger/{passenger_id}",  response={200:DeleteMessageSchema} )
def delete_flight(request, passenger_id: int):
    passenger = get_object_or_404(Passenger, id=passenger_id)
    passenger.delete()
    return 200, {"message": "Success, Passenger was deleted!"}


from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
import pendulum

#from core.api import router
from ninja import Router

from flights.models import Flight
from flights.schemas import FlightSchema, FlightCreateSchema, FlightUpdateSchema, DeleteMessageSchema
router = Router()

@router.post("/create-flight", response={200: FlightSchema})
def create_flight(request, payload: FlightCreateSchema):
    # Check if there is a connected flight and update its isConnected status
    connected_flight = Flight.objects.filter(id=payload.connection_flight_id).first() if payload.connection_flight_id else None
    
    if connected_flight:
        connected_flight.isConnected = True
        connected_flight.save()  # Save the connected flight to persist changes
    
    # Create the origin flight with the connection
    origin_flight = Flight(connection_flight=connected_flight, **payload.dict(exclude={'connection_flight_id'}))
    origin_flight.isConnected = False
    origin_flight.save()  # Save the origin flight to persist changes
    
    return origin_flight

@router.get("/get-flight/{flight_id}", response={ 200: FlightSchema })
def get_flight(request, flight_id: int):
    flight = get_object_or_404(Flight, id=flight_id)
    return flight  

    
@router.get("/get-flights", response=List[FlightSchema])
def list_flights(request):
    flights = Flight.objects.prefetch_related('connected_flight').all()
    # Update status of each flight based on the current date
    for flight in flights:
        flight.update_status()
    return flights 

@router.put("/update-flight/{flight_id}", response={ 200: FlightSchema })
def update_flight(request, flight_id: int, payload: FlightUpdateSchema ):
    flight = get_object_or_404(Flight, id=flight_id)
    for attr, value in payload.dict().items():
        setattr(flight, attr, value)
    flight.save()
    return flight


@router.delete( "/delete-flight/{flight_id}", response={200: DeleteMessageSchema} )
def delete_flight(request, flight_id: int):
    flight = get_object_or_404(Flight, id=flight_id)
    flight.delete()
    return 200, {"message": "Success, Flight was deleted!"}


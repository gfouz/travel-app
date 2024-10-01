from typing import List
from django.conf import settings 
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import pendulum

#from core.api import router
from ninja.security import HttpBearer
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from flights.models import Flight
from flights.schemas import FlightSchema, FlightCreateSchema, FlightUpdateSchema, DeleteMessageSchema
from ninja import Router


router = Router()

#  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxfQ.3VkIMOwpZFqomFnjL5G0Xcnlp6I2-jYby8fxzwDLnzU

#OJO---------------------------------------------------------------------OJO
#Asegurate de importar todas las dependencias relacionadas dentro de la función
class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload
        
        except ExpiredSignatureError:
            raise HttpError(401, "Token has expired. Please login again.")
        # Capturar cualquier otro error relacionado con el token
        except InvalidTokenError:
            raise HttpError(401, "Invalid token. Please login again.")    
        except:
            raise HttpError(401, "Not authorarized, invalid token!")
        # Capturar el error cuando el token ha expirado    


@router.get("/auth-bearer", auth=AuthBearer())
def bearer(request):
    return {"payload": request.auth}


@router.post("/create-flight", response={200: FlightSchema})
def create_flight(request, payload: FlightCreateSchema):
    # Check if there is a connected flight and update its isConnected status
    connected_flight = Flight.objects.filter(id=payload.connection_flight_id).first() if payload.connection_flight_id else None
    
    # Create the origin flight with the connection
    flight = Flight(connection_flight=connected_flight, **payload.dict(exclude={'connection_flight_id'}))
    if connected_flight:
        flight.isConnected = True
    else:
        flight.isMain = True
    flight.save()  # Save the flight to persist changes
    
    return flight

@router.get("/get-flight/{flight_id}", response={ 200: FlightSchema })
def get_flight(request, flight_id: int):
    flight = get_object_or_404(Flight, id=flight_id)
    return flight  

    
@router.get("/get-flights", response=List[FlightSchema] )
def list_flights(request):
    flights = Flight.objects.prefetch_related('connected_flight').all()
    # Update status of each flight based on the current date
    #for flight in flights:
        #flight.update_status()
    return flights 
    
@router.get("/get-flights/clients", response=List[FlightSchema] )
def list_flights_for_clients(request):
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


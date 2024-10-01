from ninja import Form
from datetime import datetime, timedelta
from ninja.responses import Response
from ninja import Schema
from users.schemas import UserSchema, UserRegister, RegisterResponse
from users.schemas import UserFullSchema, LoginResponse, UserLogin
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render

import jwt
import pendulum

from ninja.security import HttpBearer
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
#from core.api import router
from ninja import Router
from flights.models import Flight
from adjustments.models import Setting

router = Router()


# from django_ratelimit.decorators import ratelimit


# token for RobinHood user
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6IlJvYmluSG9vZCJ9.Vk-799HIsCsO4bsuitXoXYvHfUhffLxgBSZN5ZLFG-g



class Error(Schema):
    message: str


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload
        except:
            raise HttpError(401, "Not authorarized, invalid token!")


@router.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"payload": request.auth}


@router.get("/get-users", response={200: list[UserFullSchema]})
def get_user_list(request):
    users = User.objects.all()
    return users


@router.get("/allusers", response={200: list[UserSchema]})
def get_users(request):
    users = User.objects.all()
    return users


@router.post("/register")
def register_user(request, data: UserRegister):
    if User.objects.filter(username=data.username).exists():
        return {"message": "Username already exists, select other name!"}
    user = User(username=data.username, first_name=data.first_name,last_name=data.last_name, email=data.email)
    user.set_password(data.password)
    user.save()

    return 200, {"message": "created"}


# If the same IP makes >5 reqs/min, will raise Ratelimited
# @ratelimit(key="username", rate="3/m", method=["GET", "POST"], block=True)
@router.post("/login")
def login_user(request, data: UserLogin):
    setting = Setting.objects.first()
    flights = Flight.objects.all()
    for flight in flights:
        flight.update_status(setting.unavailable_days, setting.available_days)
        
    user = authenticate(request, username=data.username, password=data.password)
    
    if not user:
        raise HttpError(400, "Invalid credentials")

    # Establecer la expiración del token con Pendulum (por ejemplo, 1 hora)
    #expiration = pendulum.now().add(hours=1)
    expiration = datetime.utcnow() + timedelta(hours=1)
    
    payload = {
        "user_id": user.id,
        "exp": expiration  # Utiliza el timestamp
    }
    
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        # response = Response({"token": token})
        # response.set_cookie("access_token", token, httponly=True)
    return 200, {"id": user.id, "token": token}
    




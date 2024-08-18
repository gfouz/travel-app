"""
This module difines API endpoints for the Django Ninja endpoints.
It includes routes for handling HTTP request related to user operations

"""

from ninja.security import HttpBearer
from django.conf import settings
from ninja import Router
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from travels.schemas import ErrorMessage # type: ignore


import jwt

from ninja.errors import HttpError
from django.shortcuts import render

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








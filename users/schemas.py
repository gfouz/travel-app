from ninja import ModelSchema, Schema
from django.contrib.auth.models import User


class UserFullSchema(ModelSchema):
    class Meta:
        model = User
        exclude = ["password", "groups"]

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "username"]

    # exclude = ["last_login", "user_permissions"]
class Error(Schema):
    message: str


class UserRegister(Schema):
    username: str
    email: str
    password: str

class RegisterResponse(Schema):
    message: str


class LoginResponse(Schema):
    user_id: str
    username: str


class UserLogin(Schema):
    username: str
    password: str
    

from pydantic import BaseModel, EmailStr

class Signin(BaseModel):
    email: EmailStr
    password: str
    important: bool = None


class Signup(BaseModel):
    firstname: str
    lastname: str
    phone: str
    email1: EmailStr
    password1: str
    confirm_password: str







from fastapi import APIRouter, Request, HTTPException
from models.signin import Signin, Signup
from fastapi.responses import HTMLResponse
from config.db import conn
from schemas.signin import signinEntity, signinsEntity, signupEntity, signupsEntity
from fastapi.templating import Jinja2Templates
import re

signin = APIRouter()
signup = APIRouter()
templates = Jinja2Templates(directory="templates")


# Helper function to validate names and phone numbers
def validate_signup_data(firstname: str, lastname: str, phone: str, password: str, confirm_password: str):
    if not re.match(r'^[A-Za-z]+$', firstname):
        raise HTTPException(status_code=400, detail="First name should not contain numbers or special characters.")

    if not re.match(r'^[A-Za-z]+$', lastname):
        raise HTTPException(status_code=400, detail="Last name should not contain numbers or special characters.")

    if not re.match(r'^\d+$', phone):
        raise HTTPException(status_code=400, detail="Phone number should contain only digits.")

    if password != confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match.")


# Sign-In Form GET
@signin.get("/", response_class=HTMLResponse)
async def read_signin_page(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@signin.post("/signin")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)

    # Convert "important" checkbox value
    formDict["important"] = True if formDict.get("important") == "on" else False

    # Check if the user exists in the signup collection
    existing_user = conn.signin.signup.find_one({
        "email1": formDict["email"],
        "password1": formDict["password"]
    })

    if existing_user:
        # If user exists, save sign-in data to the signin collection
        conn.signin.signin.insert_one(formDict)
        return {"message": "Successfully signed in"}
    else:
        # If user does not exist, return an error message
        return {"message": "Please sign up"}


# Sign-Up Form GET
@signup.get("/", response_class=HTMLResponse)
async def read_signup_page(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


@signup.post("/signup")
async def create_item(request: Request):
    form = await request.form()
    formDict1 = dict(form)

    # Convert "important" checkbox value
    formDict1["important"] = True if formDict1.get("important") == "on" else False

    # Check if all fields (firstname, lastname, phone, email, password, confirm password) match an existing record
    existing_user = conn.signin.signup.find_one({
        "firstname": formDict1["firstname"],
        "lastname": formDict1["lastname"],
        "phone": formDict1["phone"],
        "email1": formDict1["email1"],
        "password1": formDict1["password1"],
        "confirm_password1": formDict1["confirm_password1"]
    })

    if existing_user:
        # If all fields match, user already has an account
        return {"message": "You already have an account"}
    else:
        # If no exact match is found, proceed with sign-up
        conn.signin.signup.insert_one(formDict1)
        return {"message": "Signup successful"}

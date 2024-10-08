from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("../static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://aachalchawhan14:aachalchawhan14@cluster1.tfe4z.mongodb.net")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.signin.signin.find({})
    for doc in docs:
        print(doc["_id"])
    return templates.TemplateResponse("signin.html", {"request": request})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

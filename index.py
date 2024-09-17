from fastapi import FastAPI
from routes.signin import signin , signup
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(signin)
app.include_router(signup)




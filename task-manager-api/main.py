from fastapi import FastAPI

APP = FastAPI()

@app.get("/")

def home():
    return {"message": "Task Manager API is running"}
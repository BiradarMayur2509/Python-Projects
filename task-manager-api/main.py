from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

# Model
class Task(BaseModel):
    task : str

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}


@app.get('/tasks')
def get_tasks():
    return {"tasks" : tasks}

# updated post 
@app.post('/tasks')
def add_task(task: Task):
    tasks.append(task.task)
    return {"message": "task added", "task": task}


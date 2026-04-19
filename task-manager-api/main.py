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
    return {"message": "task added", "task": task.task}

@app.put("/tasks/{index}")
def updated_tasks(index: int, task: Task):
    if 0 <= index < len(tasks):
        tasks[index] = task.task #fixed
        return {"message":"task updated", "task":tasks}
    return {"error": "task not found"}

@app.delete("/tasks/{index}")
def delete_task(index: int):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        return {"message": "task deleted", "task": removed}
    return {"error": "task not found"}
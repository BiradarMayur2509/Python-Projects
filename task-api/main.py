from fastapi import FastAPI # Import FastApi class
from pydantic import BaseModel

app = FastAPI() # create app ( this is your api application)

@app.get("/") # this is an endpoint (URL)
def home():
    return{"Message": "Welcome to task API"}

@app.get("/tasks")
def get_tasks():
    return {"tasks" : ["learn python", "Build Api"]}

#path parameter 
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return{"task_id" : task_id}

# query Parameter
@app.get("/search")
def search_task(name: str):
    return{"task_name": name}

#Multiple Query params
@app.get("/filter")
def filter_task(name: str, priority: int):
    return {
        "task_name" : name,
        "priority" : priority
    }
        
            
from pydantic import BaseModel

class Task(BaseModel):
    task: str

# ---------- FIX THIS ----------
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.task)
    return {"message": "task added", "tasks": tasks}
from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}


@app.get('/tasks')
def get_tasks():
    return {"tasks" : tasks}

@app.post('/tasks')
def add_task(task: str):
    tasks.append(task)
    return {"message": "task added", "task": task}


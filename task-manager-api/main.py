from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}


@app.get('/tasks')
def get_tasks():
    return {"Message": "task Manager API is running"}

@app.post('/tasks')
def add_task(task: str):
    tasks.append(task)
    return {"message": "task added", "task": task}


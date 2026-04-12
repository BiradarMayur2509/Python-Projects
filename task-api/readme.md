# 🚀 Task API Learning

## 📌 Tech Used
- Python
- FastAPI
- Uvicorn
- VS Code

---

# ✅ STEP 1: Project Setup

### Install dependencies:
```bash
pip install fastapi uvicorn
```

- **fastapi** → used to build API  
- **uvicorn** → used to run server  

---

# ✅ STEP 2: Create File

Create a file:
main.py

---

# ✅ STEP 3: First API

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Task API"}
```

## 🧠 Explanation

- `FastAPI` → framework
- `app = FastAPI()` → creates API app
- `@app.get("/")` → endpoint (URL)
- `home()` → function runs when URL is hit
- `return {}` → sends JSON response

---

# ✅ STEP 4: Run Server

```bash
uvicorn main:app --reload
```

### Open in browser:
http://127.0.0.1:8000

### Docs:
http://127.0.0.1:8000/docs

---

# ✅ STEP 5: Second Endpoint

```python
@app.get("/tasks")
def get_tasks():
    return {"tasks": ["Learn Python", "Build API"]}
```

---

# ✅ STEP 6: Path Parameter

```python
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id}
```

## 🧠 Explanation

- `{task_id}` → dynamic value in URL  
- Example:
  `/tasks/5`
- `task_id: int` → must be integer  

## 🎯 Use Case
- Get specific item (by ID)

---

# ✅ STEP 7: Query Parameter

```python
@app.get("/search")
def search_task(name: str):
    return {"task_name": name}
```

## 🧠 Example:
`/search?name=python`

## 🎯 Use Case
- Search / filter data  

---

# ✅ STEP 8: Multiple Query Parameters

```python
@app.get("/filter")
def filter_task(name: str, priority: int):
    return {
        "task_name": name,
        "priority": priority
    }
```

## 🧠 Example:
`/filter?name=study&priority=1`

---

# ⚔️ Path vs Query Parameter

| Feature | Path Param | Query Param |
|--------|-----------|------------|
| Location | `/tasks/1` | `/search?name=python` |
| Purpose | Specific item | Filter/Search |

---

# 🎯 Final Summary

- Path Param → get specific data  
- Query Param → filter/search data  
- FastAPI → connects URL with function  
- Functions → core of API  

---

# 🚀 Next Step
👉 POST API (Add Data)

# 
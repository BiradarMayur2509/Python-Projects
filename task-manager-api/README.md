# 🚀 Task Manager API (FastAPI)

## 📌 Project Overview

This is a **Task Manager API** built using FastAPI.
It allows users to create, read, update, and delete tasks (CRUD operations).

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic

---

## 🎯 Features

* Add new tasks
* View all tasks
* Update existing tasks
* Delete tasks
* Uses **unique ID** for each task
* JSON-based request/response

---

## 📂 Project Structure

task-manager-api/
│── main.py
│── README.md

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install fastapi uvicorn
```

### 2. Run server

```bash
uvicorn main:app --reload
```

### 3. Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

### ✅ GET /tasks

Get all tasks

### ✅ POST /tasks

Add a new task

Request body:

```json
{
  "task": "Learn FastAPI"
}
```

---

### ✅ PUT /tasks/{task_id}

Update a task

```json
{
  "task": "Updated Task"
}
```

---

### ✅ DELETE /tasks/{task_id}

Delete a task

---

## 🧠 How it Works

* Tasks are stored in a list
* Each task has a unique ID
* CRUD operations are handled using FastAPI routes

---

## 📌 Example Response

```json
{
  "tasks": [
    {
      "id": 1,
      "task": "Study Python"
    }
  ]
}
```

---

## 🚀 Future Improvements

* Add database (SQLite / PostgreSQL)
* Add authentication
* Add task status (completed / pending)
* Build frontend UI

---

## 👨‍💻 Author

Biradar Mayur

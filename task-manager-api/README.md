# 🚀 Task Manager API (FastAPI)

## 📌 Project Overview

This is a simple **Task Manager API** built using FastAPI.
It allows users to perform basic CRUD operations (Create, Read, Update, Delete) on tasks.

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
* Update tasks using index
* Delete tasks using index
* JSON-based request and response

---

## 📂 Project Structure

task-manager-api/
│── main.py
│── README.md

---

## ▶️ How to Run

### 1. Install dependencies

```bash id="o7rr41"
pip install fastapi uvicorn
```

### 2. Run the server

```bash id="q38mb2"
uvicorn main:app --reload
```

### 3. Open Swagger UI

```id="1nt5lh"
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

### ✅ GET /tasks

Get all tasks

---

### ✅ POST /tasks

Add a new task

Request body:

```json id="5kk22c"
{
  "task": "Learn FastAPI"
}
```

---

### ✅ PUT /tasks/{index}

Update a task using index

Example:

```json id="3pdsfa"
{
  "task": "Updated Task"
}
```

---

### ✅ DELETE /tasks/{index}

Delete a task using index

---

## 🧠 How it Works

* Tasks are stored in a Python list
* Each task is accessed using its index
* CRUD operations are handled using FastAPI routes

---

## 📌 Example Response

```json id="4tqk7m"
{
  "tasks": [
    "Study Python",
    "Go to Gym",
    "Learn FastAPI"
  ]
}
```

---

## ⚠️ Limitations

* Uses index instead of unique ID
* Data is temporary (resets when server restarts)
* No database integration

---

## 🚀 Future Improvements

* Use unique IDs instead of index
* Add database (SQLite/PostgreSQL)
* Add authentication
* Build frontend UI

---

## 👨‍💻 Author

Mayur Biradar

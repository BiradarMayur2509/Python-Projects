# 🔗 URL Shortener API (FastAPI)

## 📌 Project Overview

This is a **URL Shortener API** built using FastAPI.
It converts long URLs into short, shareable links and redirects users to the original URL.

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic

---

## 🎯 Features

* Convert long URL → short URL
* Redirect short URL → original URL
* Automatic short code generation
* Handles invalid URLs
* Dynamic routing

---

## 📂 Project Structure

url-shortener-api/
│── main.py
│── README.md

---

## ▶️ How to Run

### 1. Install dependencies

```bash id="z4o3il"
pip install fastapi uvicorn
```

### 2. Run server

```bash id="i0twf6"
uvicorn main:app --reload
```

### 3. Open Swagger UI

```id="9n2p38"
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

### ✅ GET /

Check API status

---

### ✅ POST /shorten

Convert long URL to short URL

Request:

```json id="9jbfdm"
{
  "url": "https://google.com"
}
```

Response:

```json id="eq1p82"
{
  "short_url": "http://127.0.0.1:8000/abc123",
  "original_url": "https://google.com"
}
```

---

### ✅ GET /{code}

Redirect to original URL

Example:

```id="3paz8z"
http://127.0.0.1:8000/abc123
```

---

## 🧠 How it Works

* Generates a random short code
* Stores mapping in dictionary
* Uses dynamic routing for redirect

---

## ⚠️ Limitations

* Data is temporary (resets on restart)
* No database used
* No authentication

---

## 🚀 Future Improvements

* Add database (SQLite/PostgreSQL)
* Custom short URLs
* Expiry time for links
* Analytics (click tracking)

---

## 👨‍💻 Author

Biradar Mayur

from fastapi import FastAPI
from pydantic import BaseModel
import random 
import string
from fastapi.responses import RedirectResponse

app = FastAPI()
url_db = {}

# Model
class URLRequest(BaseModel):
    url : str

# generate short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@app.get('/')
def home():
    return {"Message" : "Url shortener API is running"}

# post: shorten url

@app.post("/shorten")
def short_url(request: URLRequest):
    url = request.url
    if not url.startswith("http"):
        url = "https://" + url
        
    code = generate_code()
    url_db[code] = url
    
    short_url = f"http://127.0.0.1:8000/{code}"
    
    return {
        "short_url" : short_url,
        "original_url" : request.url
    }

# redirect 
@app.get("/{code}")
def redirect_url(code: str):
    if code in url_db:
        return RedirectResponse(url_db[code])
    return {"error" : "URL not found"}
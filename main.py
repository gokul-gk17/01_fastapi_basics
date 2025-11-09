from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend Journey Starts 🚀"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"greeting": f"Hello, {name}! Welcome to FastAPI."}

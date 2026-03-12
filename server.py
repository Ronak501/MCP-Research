from fastapi import FastAPI
from tools.calculator import add_numbers
from tools.weather import get_weather

app = FastAPI()

@app.get("/add")
def add(a: int, b: int):
    return {"result": add_numbers(a, b)}

@app.get("/weather")
def weather(city: str):
    return {"result": get_weather(city)}
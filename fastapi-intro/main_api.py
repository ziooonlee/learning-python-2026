from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello, World!"}

@app.get("/items/{item.id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/greet/{name}")
def greet_person(name: str):
    return{"message": f"Hello, {name}!"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return{"result": a+b}

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user (user: User):
    return{"message": f"Created user {user.name}, age {user.age}"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str=None):
    return {"item_id": item_id, "q": q}


@app.get("/hello/{name}")
def say_hello(name : str):
    return {"message": f"Hello, {name}!"}

@app.get("/hello/spanish/{name}")
def say_hello(name : str):
    return {"message": f"Hello, {name}!"}


@app.get("/goodbye/{name}")
def say_goodbye(name : str):
    return {"message": f"Goodbye, {name}"}

@app.get("/goodbye/spanish/{name}")
def say_goodbye_spanish(name : str):
    return {"message": f"Adios, {name}"}
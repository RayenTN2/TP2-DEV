from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "it works !"}


@app.get("/addition")
def add_numbers(a: int, b: int):
    return {"result a+b=": a + b, "developer": "Dev1"}


@app.post("/divide")
def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result a/b=": a / b, "developer": "Leader"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "it works !"}

@app.get("/addition")
def add_numbers(a: int, b: int):
    return {"result a+b=": a + b, "developer": "Dev1"}

<<<<<<< HEAD
=======
@app.post("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result a*b=": a * b, "developer": "Dev2"}
>>>>>>> main

@app.post("/divide")
def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result a/b=": a / b, "developer": "Leader"}

<<<<<<< HEAD
=======

>>>>>>> main
@app.delete("/remove/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}
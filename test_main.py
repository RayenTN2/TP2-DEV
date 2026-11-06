from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}

def test_soustraction():
    response = client.get("/soustract/?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_addition():
    response = client.get("/addition?a=4&b=2")
    assert response.status_code == 200
    assert response.json() == {"result a+b=": 6, "developer": "Dev1"}

def test_multiply():
    response = client.post("/multiply?a=3&b=3")
    assert response.status_code == 200
    assert response.json() == {"result a*b=": 9, "developer": "Dev2"}

def test_divide():
    response = client.post("/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json() == {"result a/b=": 5.0, "developer": "Leader"}

def test_divide_by_zero():
    response = client.post("/divide?a=10&b=0")
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero is not allowed"}

def test_delete_item():
    response = client.delete("/remove/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 deleted successfully"}

def test_update_item():
    response = client.put("/update/1?name=Laptop")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 updated successfully", "new_name": "Laptop"}
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_and_delete_todo():
    # Add a todo
    response = client.post("/todo/", json={
        "title": "Test Task",
        "description": "This is a test"
    })
    assert response.status_code == 200
    todo = response.json()
    assert "id" in todo
    assert todo["title"] == "Test Task"

    # Get todos
    response = client.get("/todo/")
    assert response.status_code == 200
    todos = response.json()
    assert any(t["id"] == todo["id"] for t in todos)

    # Delete it
    response = client.delete(f"/todo/{todo['id']}")
    assert response.status_code == 200

    # Confirm deletion
    response = client.get("/todo/")
    ids = [t["id"] for t in response.json()]
    assert todo["id"] not in ids

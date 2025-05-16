from fastapi.testclient import TestClient
from app.main import app



client=TestClient(app)

def test_create_todos():
    response=client.post("/todo/",json={
        "title":"Test task",
        "description":"Description of the test task"
    })
    assert response.status_code==201
    data = response.json()
    assert data["title"] == "Test task"
    assert data["description"]=="Description of the test task"

def test_get_todos():
    response=client.get("/todo")
    assert response.status_code==200
    assert isinstance(response.json(),list)

def test_update_todos():
    create=client.post("/todo",json={
        "title":"Test task",
        "description":"Description of the test task"
    })
    todo_id=create.json()["id"]

    response=client.patch(f"/todo/{todo_id}",json={
        "description":"updated Description of the test task"
    })

    assert response.status_code==200
    assert response.json()["description"]=="updated Description of the test task"

def test_delete_todo():
    create=client.post("/todo",json={
        "title":"College",
        "description":"Assignments"
    })
    todo_id=create.json()["id"]

    response=client.delete(f"/todo/{todo_id}")
    assert response.status_code==200

    get_response=client.get(f"/todo/{todo_id}")
    assert get_response.status_code==404


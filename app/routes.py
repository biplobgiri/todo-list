from fastapi import APIRouter, HTTPException
from app.schemas import Todo
from app.storage import todos, generate_id, current_id  

router = APIRouter(prefix="/todo", tags=["Todos"])

@router.post("/", status_code=201)
def create_todo(todo: Todo):
    todo_id = generate_id()
    todos[todo_id] = todo
    return {"id": todo_id, "message": "Todo created"}

@router.get("/")
def get_all_todos():
    return [{"id": tid, **todo.dict()} for tid, todo in todos.items()]

@router.delete("/{todo_id}")
def delete_todo(todo_id: int): 
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return {"message": "Todo deleted"}

@router.delete("/clear", status_code=200)
def clear_all_todos():
    global current_id
    todos.clear()
    current_id = 1  
    return {"message": "All todos cleared"}
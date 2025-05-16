from fastapi import APIRouter,HTTPException
from app.schemas import Todo,TodoUpdate
from app.storage import todos, generate_id,current_id

router=APIRouter(prefix='/todo',tags=["Todos"])


    

@router.post("/",status_code=201)
def create_todo(todo_input:Todo):
    todo_id=generate_id()
    todos[todo_id]=todo_input
    return {"id":todo_id,**todo_input.model_dump(),"message":"todo created"}

@router.get("/",status_code=200)
def get_all_todos():
    return [{"id":tid,**todo.model_dump()} for tid,todo in (todos.items())]

@router.get("/{todo_id}",status_code=200)
def get_todo_item(todo_id:int):
    if todo_id in todos: 
        #indexing to be checked
        return {"id":todo_id,**todos[todo_id].model_dump()}
    raise HTTPException(status_code=404,detail="invalid id")
    
@router.delete("/{todo_id}")
def delete_item(todo_id:int):
    if todo_id not in todos:
        raise HTTPException(status_code=404,detail="item not found")
    del todos[todo_id]

@router.patch("/{todo_id}",status_code=200)
def update_item(todo_id: int,todo_input: TodoUpdate):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail='item not found')
    existing=todos[todo_id]
    update_data=todo_input.model_dump(exclude_unset=True)

    for field,value in update_data.items():
        setattr(existing,field,value)   

    return {"id":todo_id, **existing.model_dump(), "message":"Todo updated"} 

@router.patch("/completed/{todo_id}",status_code=200)   
def update_status(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404,detail='item not found')
    todos[todo_id]["status"]=True

@router.delete("/clear", status_code=200)
def clear_all():
    global current_id
    todos.clear()
    current_id=1
    return{"Message":"All todos have been cleared"}


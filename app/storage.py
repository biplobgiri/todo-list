from app.schemas import Todo
from typing import Dict

todos: Dict[int, Todo] = {}  
current_id = 1  

def generate_id() -> int:
    global current_id
    new_id=current_id
    current_id += 1
    return new_id
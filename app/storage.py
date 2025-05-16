from app.schemas import Todo
from typing import Dict

current_id=1
todos: Dict[int,Todo]={}

def generate_id()->int:
    global current_id
    new_id=current_id
    current_id=current_id+1
    return new_id

    
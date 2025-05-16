from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    title:str
    description:str
    status:bool= False

class TodoUpdate(BaseModel):
    title: Optional[str] =None
    description: Optional[str]=None
    status:Optional[bool]=None

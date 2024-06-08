# from pydantic import BaseModel

# class ToDo(BaseModel):
#     id:int
    
#     item:str


from pydantic import BaseModel

class ToDo(BaseModel):
    id: int = None
    name: str
    contents: str
    timestamp: str = None


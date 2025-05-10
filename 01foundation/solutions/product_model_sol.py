from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True






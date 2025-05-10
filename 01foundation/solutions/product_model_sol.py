from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


todo = Todo(id=1, name='jjkd', price=1, in_stock=True)
print(todo)




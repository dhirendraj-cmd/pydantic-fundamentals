from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {"id": 'e1', 'name': 'kb', 'is_active': 'false'}

user = User(**input_data)

print(user)
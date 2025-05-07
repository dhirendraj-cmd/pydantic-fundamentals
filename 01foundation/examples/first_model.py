from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool

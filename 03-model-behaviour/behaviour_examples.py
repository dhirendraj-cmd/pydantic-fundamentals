from pydantic import BaseModel, field_validator, model_validator, computed_field


# field_validator
class User(BaseModel):
    username: str

    @field_validator('username')
    def username_validation(cls, v): #v means value
        if len(v) < 3:
            raise ValueError("Username should be min of 3 characters")
        return v
        
        #  have to implement uniqueness of username


user = User(username="acd")
print(user.username)


# model_validator
class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match!!")
        return values


register = SignUpData(password="abcd", confirm_password="abcd")
print(register)


# computed_field
class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

prod = Product(price=22, quantity=4)
print(prod.total_price)



"""
    Note: 
    1. field_validator runs before pydantic itself 
    2. model_validator runs after all custom validations happen and it has mode='after'
"""



from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Optional

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int
    rate_per_night: float

    @field_validator('nights')
    def nights_validator(cls, values):
        if values < 1:
            raise ValueError("Atleast stay 1 night bro in your dream destination.")
        return values
    
    
    
    @computed_field
    @property
    def total_amout(self) -> float:
        return self.nights * self.rate_per_night
    

print(Booking(user_id=1, room_id=2, nights=8, rate_per_night=48))


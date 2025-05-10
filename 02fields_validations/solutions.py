from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    emp_id: int
    emp_name: str = Field(..., 
                          min_length=3, 
                          max_length=50, 
                          description="Employee name",
                          examples="Dhirendr Jha"
                          )
    emp_dept: Optional[str] = 'General'
    emp_salary: float = Field(..., ge=10000, le=300000)

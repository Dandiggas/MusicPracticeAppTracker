
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

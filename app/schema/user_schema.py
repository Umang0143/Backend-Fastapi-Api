from pydantic import BaseModel, EmailStr

class Signup(BaseModel):
    name: str
    email: EmailStr
    mobile: str
    address: str
    fileUrl: str
    city: str

class User(BaseModel):
    name: str
    email: EmailStr
    mobile: str
    address: str
    city: str
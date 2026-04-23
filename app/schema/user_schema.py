# from typing import Optional
# from pydantic import BaseModel, EmailStr

# class Signup(BaseModel):
#     name: str
#     email: EmailStr
#     password: str
#     mobile: str
#     address: Optional[str] = None
#     fileUrl: Optional[str] = None

# class UserUpdate(BaseModel):
#     name: str
#     email: EmailStr
#     mobile: str

# class Login(BaseModel):
#     email: EmailStr
#     password: str
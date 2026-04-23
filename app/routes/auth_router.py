# from fastapi import APIRouter, HTTPException
# from app.schema.user_schema import Login
# from app.core.security import create_token
# router = APIRouter(prefix="/api/auth", tags=["auth"])
 
# users = [
#     {"email": "test@gmail.com", "password": "1234", "name": "Test User"}
# ]
 
# @router.post("/login")
# def login(data: Login):
 
#     for user in users:
#         if user["email"] == data.email and user["password"] == data.password:
 
#             token = create_token({
#                 "sub": user["email"],
#                 "name": user["name"]
#             })
 
#             return {
#                 "message": "Login successful",
#                 "access_token": token,
#                 "token_type": "bearer"
#             }
 
#     raise HTTPException(status_code=401, detail="Invalid credentials")
 
# from fastapi import APIRouter, Depends
# from app.schema.user_schema import Signup, UserUpdate
# from app.services import user_service
# from app.routes.deps import get_current_user

# router = APIRouter()

# @router.post("/signup")
# def signup(user: Signup):
#     user_service.create_user(user)
#     return {"message": "User Registered"}

# @router.get("/getusers")
# def get_users(user=Depends(get_current_user)):
#     return user_service.get_users()

# @router.put("/update/{id}")
# def update(id: int, data: UserUpdate, user=Depends(get_current_user)):
#     user_service.update_user(id, data)
#     return {"message": "Updated"}

# @router.delete("/delete/{id}")
# def delete(id: int, user=Depends(get_current_user)):
#     user_service.delete_user(id)
#     return {"message": "Deleted"}


# from fastapi import APIRouter, Depends
# from app.schema import user_schema
# from app.services.user_service import UserService
# from app.core.security import verify_token
 
# router = APIRouter(prefix="/api/users", tags=["users"])
# service = UserService()
# @router.post("/")
# def create_user(user: user_schema.Signup, token=Depends(verify_token)):
#     service.create_user(user)
#     return {"message": "User Created"}
 
 
# @router.get("/")
# def get_users(token=Depends(verify_token)):
#     rows = service.get_users()
 
#     return [
#         {
#             "id": r["id"],
#             "name": r["name"],
#             "email": r["email"],
#             "mobile": r["mobile"]
#         }
#         for r in rows
#     ]
 
 
# @router.put("/{id}")
# def update_user(id: int, user: user_schema.UserUpdate, token=Depends(verify_token)):
#     service.update_user(id, user)
#     return {"message": "User Updated"}
 
 
# @router.delete("/{id}")
# def delete_user(id: int, token=Depends(verify_token)):
#     service.delete_user(id)
#     return {"message": "User Deleted"}


# from fastapi import APIRouter, Depends
# from app.schema.user_schema import Signup, UserUpdate
# from app.services import user_service
# from app.routes.deps import get_current_user

# router = APIRouter()

# @router.post("/signup")
# def signup(user: Signup):
#     user_service.register_user(user)
#     return {"message": "User Registered"}

# @router.get("/getusers")
# def get_users(user=Depends(get_current_user)):
#     return user_service.get_all_users()

# @router.put("/update/{id}")
# def update(id: int, data: UserUpdate, user=Depends(get_current_user)):
#     user_service.update_user(id, data)
#     return {"message": "Updated"}

# @router.delete("/delete/{id}")
# def delete(id: int, user=Depends(get_current_user)):
#     user_service.delete_user(id)
#     return {"message": "Deleted"}
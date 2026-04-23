# from fastapi import Header, HTTPException
# from app.auth.cognito import verify_token

# def get_current_user(Authorization: str = Header(...)):
#     if not Authorization:
#         raise HTTPException(status_code=401, detail="No token")

#     token = Authorization.replace("Bearer ", "")
#     return verify_token(token)

# from fastapi import Header, HTTPException
# from app.auth.cognito import verify_token

# def get_current_user(Authorization: str = Header(...)):
#     if not Authorization:
#         raise HTTPException(status_code=401, detail="No token")

#     token = Authorization.replace("Bearer ", "")
#     return verify_token(token)
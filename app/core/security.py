# from passlib.context import CryptContext



# from jose import jwt
# from datetime import datetime, timedelta
# from fastapi import Header, HTTPException
# from app.core.config import SECRET_KEY, ALGORITHM




# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(password: str):
#     return pwd_context.hash(password)




 
# def create_token(data: dict):
#     payload = data.copy()
#     payload.update({
#         "exp": datetime.utcnow() + timedelta(hours=2)
#     })
 
#     return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
 
 
# def verify_token(authorization: str = Header(None)):
#     if not authorization:
#         raise HTTPException(status_code=401, detail="No token")
 
#     token = authorization.replace("Bearer ", "")
 
#     try:
#         return jwt.get_unverified_claims(token)
#     except:
#         raise HTTPException(status_code=401, detail="Invalid token")
 
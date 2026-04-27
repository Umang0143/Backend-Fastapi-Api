from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)


# import pyodbc
# import os
# import jwt
# import requests

# from fastapi import FastAPI, HTTPException, Depends
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from pydantic import BaseModel, EmailStr
# from dotenv import load_dotenv



# # -------------------- INIT --------------------
# # Initialize the FastAPI application and set up HTTP Bearer authentication for securing endpoints that require token verification.
# app = FastAPI()
# security = HTTPBearer()

# load_dotenv(".env")

# # CORS Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -------------------- ENV --------------------
# # Load AWS Cognito configuration from environment variables
# COGNITO_REGION = os.getenv("AWS_REGION")
# USER_POOL_ID = os.getenv("USER_POOL_ID")
# APP_CLIENT_ID = os.getenv("APP_CLIENT_ID")

# # -------------------- JWKS --------------------
# # Construct the JWKS URL based on the Cognito region and user pool ID. This URL is used to retrieve the JSON Web Key Set (JWKS) for verifying JWT tokens issued by AWS Cognito.
# JWKS_URL = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{USER_POOL_ID}/.well-known/jwks.json"

# def get_jwks():
#     return requests.get(JWKS_URL).json()

# # -------------------- TOKEN VERIFY --------------------
# # This function verifies the JWT token sent in the Authorization header. It retrieves the JWKS from AWS Cognito, extracts the appropriate public key, and decodes the token to validate it and extract the payload.
# def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
#     token = credentials.credentials

#     try:
#         jwks = get_jwks()

#         headers = jwt.get_unverified_header(token)
#         kid = headers["kid"]

#         key = next(k for k in jwks["keys"] if k["kid"] == kid)
#         public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)

#         payload = jwt.decode(
#             token,
#             public_key,
#             algorithms=["RS256"],
#             audience=APP_CLIENT_ID
#         )

#         return payload

#     except Exception:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")


# # -------------------- DB CONNECTION --------------------
# # Establish a connection to the SQL Server database using pyodbc and environment variables for configuration.
# def get_db_connection():
#     return pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#         f"SERVER={os.getenv('DB_SERVER')};"
#         f"DATABASE={os.getenv('DB_DATABASE')};"
#         f"UID={os.getenv('DB_UID')};"
#         f"PWD={os.getenv('DB_PWD')};"
#         "Encrypt=no;"
#         "Timeout=30;"
#     )

# # -------------------- MODELS --------------------
# # Pydantic models for request validation and response formatting
# class Signup(BaseModel):
#     name: str
#     email: EmailStr
#     mobile: str
#     address: str
#     fileUrl: str
#     city: str

# class User(BaseModel):
#     name: str
#     email: EmailStr
#     mobile: str
#     address: str
#     city: str
 
# # -------------------- CREATE --------------------
# # This endpoint allows users to sign up by providing their details. It does not require authentication.
# @app.post("/signup")
# def register(user: Signup):
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "EXEC Research.RegisterUser ?, ?, ?, ?, ?, ?",
#             user.name,
#             user.email,
#             user.mobile,
#             user.address,
#             user.fileUrl,
#             user.city
#         )

#         conn.commit()

#         return {"message": "User Registered Successfully"}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# # -------------------- READ (ALL) --------------------
# # This endpoint retrieves all users from the database and requires authentication via the verify_token dependency.
# @app.get("/getusers")
# def get_students(user=Depends(verify_token)):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("EXEC GetUsers")

#     columns = [col[0] for col in cursor.description]
#     rows = cursor.fetchall()

#     result=[]

#     for row in rows:
#       result.append(
#        dict(zip(columns,row))
#       )

#     return result
 
# # -------------------- UPDATE --------------------
# # This endpoint updates a user's information by ID and requires authentication via the verify_token dependency.
# @app.put("/update/{id}")
# def update_user(id: int, data: User, user=Depends(verify_token)):
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         "EXEC Research.UpdateUser ?, ?, ?, ?, ?, ?",
#         id,
#         data.name,
#         data.email,
#         data.mobile,
#         data.address,
#         data.city
#     )

#     conn.commit()

#     return {"message": "Updated Successfully"}


# # -------------------- DELETE --------------------
# # This endpoint deletes a user by ID and requires authentication via the verify_token dependency.
# @app.delete("/delete/{id}")
# def delete_user(id: int, user=Depends(verify_token)):
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     cursor.execute("EXEC DeleteUser ?", id)
#     conn.commit()

#     return {"message": "Deleted Successfully"}


# # -------------------- PAGINATION --------------------
# # This endpoint supports pagination, searching by name, email, or city, and returns the total count of matching records.
# @app.get("/users")
# def get_users(
#     page: int = 1,
#     limit: int = 8,
#     search: str = "",
#     user=Depends(verify_token)
# ):
#     try:
#         conn=get_db_connection()
#         cursor=conn.cursor()

#         offset = (page - 1) * limit

#         query = """
#         SELECT * FROM Research.Registration
#         WHERE
#             (? = '' OR name LIKE ? OR email LIKE ? OR city LIKE ?)
#         ORDER BY id
#         OFFSET ? ROWS
#         FETCH NEXT ? ROWS ONLY
#         """

#         search_param = f"%{search}%"

#         cursor.execute(
#             query,
#             search,
#             search_param,
#             search_param,
#             search_param,
#             offset,
#             limit
#         )

#         columns = [col[0] for col in cursor.description]
#         rows = cursor.fetchall()

#         data = [dict(zip(columns, row)) for row in rows]

#         # total count with search
#         cursor.execute(
#             """
#             SELECT COUNT(*) FROM Research.Registration
#             WHERE
#                 (? = '' OR name LIKE ? OR email LIKE ? OR city LIKE ?)
#             """,
#             search,
#             search_param,
#             search_param,
#             search_param
#         )

#         total = cursor.fetchone()[0]

#         return {
#             "data": data,
#             "total": total,
#             "page": page,
#             "limit": limit
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
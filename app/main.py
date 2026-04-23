# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.routes import user_routes

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(user_routes.router)


import pyodbc
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from passlib.context import CryptContext

app = FastAPI()

load_dotenv(".env")

# Database connection parameters from environment variables
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_UID")
password = os.getenv("DB_PWD")


# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
def hash_password(password: str):
    return pwd_context.hash(password)


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Connection to SQL Server
connection = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=no;"
)

# CREATE (RegisterUser)
class Signup(BaseModel):
    name: str
    email: EmailStr
    mobile: str
    address: str
    fileUrl: str
    city: str
 
@app.post("/signup")
def register(user: Signup):
    try:
        cursor = connection.cursor()

        cursor.execute(
            "EXEC Research.RegisterUser ?, ?, ?, ?, ?",
            user.name,
            user.email,
            user.mobile,
            user.address,
            user.fileUrl,
            user.city
        )

        connection.commit()

        return {"message": "User Registered Successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# READ (GetUsers)
@app.get("/getusers")
def get_students():

    cursor = connection.cursor()

    cursor.execute(
      "EXEC GetUsers"
    )

    columns = [
      column[0]
      for column in cursor.description
    ]

    rows = cursor.fetchall()

    result=[]

    for row in rows:
      result.append(
       dict(zip(columns,row))
      )

    return result



# UPDATE (UpdateUser)
class User(BaseModel):
    name: str
    email: EmailStr
    mobile: str
 
@app.put("/update/{id}")
def update_user(
 id:int,
 data:User
):

    cursor=connection.cursor()

    cursor.execute(
    """
    EXEC Research.UpdateUser
    ?,?,?,?,?
    """,

    id,
    data.name,
    data.email,

    "",

    data.mobile
    )

    connection.commit()

    return {
      "message":"Updated Successfully"
    }



# DELETE (DeleteUser)
@app.delete("/delete/{id}")
def delete_user(id:int):

    cursor=connection.cursor()

    cursor.execute(
      "EXEC DeleteUser ?",
      id
    )

    connection.commit()

    return {
      "message":"Deleted Successfully"
    }


@app.get("/users")
def get_users(page: int = 1, limit: int = 10):
    try:
        cursor = connection.cursor()

        offset = (page - 1) * limit

        query = f"""
        SELECT * FROM Research.Registration
        ORDER BY id
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY
        """

        cursor.execute(query, offset, limit)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        result = [dict(zip(columns, row)) for row in rows]

        # Total count
        cursor.execute("SELECT COUNT(*) FROM Research.Registration")
        total = cursor.fetchone()[0]

        return {
            "data": result,
            "total": total,
            "page": page,
            "limit": limit
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
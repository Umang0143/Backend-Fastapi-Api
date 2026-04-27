from fastapi import APIRouter, Depends, HTTPException
from app.core.db import get_db_connection
from app.core.security import verify_token
from app.schema.user_schema import Signup, User

router = APIRouter()

# ---------------- SIGNUP ----------------
@router.post("/signup")
def register(user: Signup):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "EXEC Research.RegisterUser ?, ?, ?, ?, ?, ?",
            user.name,
            user.email,
            user.mobile,
            user.address,
            user.fileUrl,
            user.city
        )

        conn.commit()
        return {"message": "User Registered Successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------------- GET USERS (PAGINATION + SEARCH) ----------------
@router.get("/users")
def get_users(
    page: int = 1,
    limit: int = 8,
    search: str = "",
    user=Depends(verify_token)
):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        offset = (page - 1) * limit

        query = """
        SELECT * FROM Research.Registration
        WHERE (? = '' OR name LIKE ? OR email LIKE ? OR city LIKE ?)
        ORDER BY id
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY
        """

        search_param = f"%{search}%"

        cursor.execute(
            query,
            search,
            search_param,
            search_param,
            search_param,
            offset,
            limit
        )

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        data = [dict(zip(columns, row)) for row in rows]

        cursor.execute(
            """
            SELECT COUNT(*) FROM Research.Registration
            WHERE (? = '' OR name LIKE ? OR email LIKE ? OR city LIKE ?)
            """,
            search,
            search_param,
            search_param,
            search_param
        )

        total = cursor.fetchone()[0]

        return {
            "data": data,
            "total": total,
            "page": page,
            "limit": limit
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------------- UPDATE ----------------
@router.put("/update/{id}")
def update_user(id: int, data: User, user=Depends(verify_token)):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "EXEC Research.UpdateUser ?, ?, ?, ?, ?, ?",
        id,
        data.name,
        data.email,
        data.mobile,
        data.address,
        data.city
    )

    conn.commit()

    return {"message": "Updated Successfully"}


# ---------------- DELETE ----------------
@router.delete("/delete/{id}")
def delete_user(id: int, user=Depends(verify_token)):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC DeleteUser ?", id)
    conn.commit()

    return {"message": "Deleted Successfully"}




@router.get("/getusers")
def get_students(user=Depends(verify_token)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC GetUsers")

    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    result=[]

    for row in rows:
      result.append(
       dict(zip(columns,row))
      )

    return result
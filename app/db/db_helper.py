# from app.db.Connection import get_connection

# def call_procedure(proc_name, params=None, fetch=False):
#     conn = get_connection()
#     cursor = conn.cursor()

#     try:
#         if params:
#             placeholders = ",".join(["?"] * len(params))
#             query = f"EXEC {proc_name} {placeholders}"
#             cursor.execute(query, params)
#         else:
#             query = f"EXEC {proc_name}"
#             cursor.execute(query)

#         # 👉 GET case
#         if fetch:
#             columns = [column[0] for column in cursor.description]
#             result = []

#             for row in cursor.fetchall():
#                 result.append(dict(zip(columns, row)))

#             return result

#         # 👉 INSERT / UPDATE / DELETE
#         conn.commit()
#         return {"message": "Success"}

#     except Exception as e:
#         conn.rollback()
#         return {"error": str(e)}

#     finally:
#         conn.close()


# import pyodbc
# from app.core.config import DB_URL
 
# def execute_sp(proc_name, params=(), fetch=False):
#     conn = pyodbc.connect(DB_URL)
   
#     try:
#         cursor = conn.cursor()
#         cursor.execute("SELECT DB_NAME()")
#         print("CONNECTED DB:", cursor.fetchone()[0])
#         query = f"EXEC {proc_name} " + ",".join(["?"] * len(params))
#         cursor.execute(query, params)
 
#         if fetch:
#             columns = [col[0] for col in cursor.description]
#             rows = cursor.fetchall()
#             return [dict(zip(columns, row)) for row in rows]
 
#         conn.commit()
 
#     finally:
#         conn.close()
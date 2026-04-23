# from app.db.db_helper import call_procedure

# def register_user(user):
#     return call_procedure(
#         "Research.RegisterUser",
#         (user.name, user.email, user.password, user.mobile)
#     )

# def get_users():
#     return call_procedure("GetUsers", fetch=True)

# def update_user(id, data):
#     return call_procedure(
#         "Research.UpdateUser",
#         (id, data.name, data.email, "", data.mobile)
#     )

# def delete_user(id):
#     return call_procedure("DeleteUser", (id,))


# from app.db.Connection import get_connection

# def create_user(user, password_hash):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         "EXEC Research.RegisterUser ?, ?, ?, ?, ?, ?",
#         (user.name, user.email, password_hash, user.mobile, user.address, user.fileUrl)
#     )

#     conn.commit()
#     conn.close()


# def get_users():
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("EXEC GetUsers")

#     columns = [col[0] for col in cursor.description]
#     rows = cursor.fetchall()

#     conn.close()

#     return [dict(zip(columns, row)) for row in rows]


# def update_user(id, data):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute(
#         "EXEC Research.UpdateUser ?,?,?,?,?",
#         id,
#         data.name,
#         data.email,
#         "",
#         data.mobile
#     )

#     conn.commit()
#     conn.close()


# def delete_user(id):
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("EXEC DeleteUser ?", id)

#     conn.commit()
#     conn.close()
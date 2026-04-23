# from passlib.context import CryptContext
# from app.repositories import user_repo

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def register_user(user):
#     hashed_password = pwd_context.hash(user.password)
#     user.password = hashed_password

#     return user_repo.register_user(user)

# def get_users():
#     return user_repo.get_users()

# def update_user(id, data):
#     return user_repo.update_user(id, data)

# def delete_user(id):
#     return user_repo.delete_user(id)


# from app.db.Connection import connection
# from app.core.security import hash_password

# def create_user(user):
#     cursor = connection.cursor()

#     passwordhash = hash_password(user.password)

#     cursor.execute(
#         "EXEC Research.RegisterUser ?, ?, ?, ?, ?, ?",
#         (user.name, user.email, passwordhash, user.mobile, user.address, user.fileUrl)
#     )

#     connection.commit()


# def get_users():
#     cursor = connection.cursor()
#     cursor.execute("EXEC GetUsers")

#     columns = [col[0] for col in cursor.description]
#     rows = cursor.fetchall()

#     return [dict(zip(columns, row)) for row in rows]


# def update_user(id, data):
#     cursor = connection.cursor()

#     cursor.execute(
#         "EXEC Research.UpdateUser ?,?,?,?,?",
#         id,
#         data.name,
#         data.email,
#         "",
#         data.mobile
#     )

#     connection.commit()


# def delete_user(id):
#     cursor = connection.cursor()

#     cursor.execute("EXEC DeleteUser ?", id)

#     connection.commit()


# from app.repositories import user_repo
# from app.core.security import hash_password

# def register_user(user):
#     password_hash = hash_password(user.password)
#     user_repo.create_user(user, password_hash)

# def get_all_users():
#     return user_repo.get_users()

# def update_user(id, data):
#     user_repo.update_user(id, data)

# def delete_user(id):
#     user_repo.delete_user(id)
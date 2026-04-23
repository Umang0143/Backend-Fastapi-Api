# import pyodbc
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_connection():
#     return pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#         f"SERVER={os.getenv('DB_SERVER')};"
#         f"DATABASE={os.getenv('DB_DATABASE')};"
#         f"UID={os.getenv('DB_UID')};"
#         f"PWD={os.getenv('DB_PWD')};"
#         "Encrypt=no;"
#     )


import pyodbc
from app.core.config import DB_SERVER, DB_DATABASE, DB_UID, DB_PWD

connection = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={DB_SERVER};"
    f"DATABASE={DB_DATABASE};"
    f"UID={DB_UID};"
    f"PWD={DB_PWD};"
    "Encrypt=no;"
)
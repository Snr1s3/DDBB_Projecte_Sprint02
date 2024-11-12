# Autor: Alba Segura
# Data: 9/10/24

#Importem la funcio db_client de client
from client import db_client

#Funció per a retornar tots els users
def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users
    except Exception as e:
        print(f"Error reading from database: {e}")
        print(f"Error reading from database: ")
        return []

#Funció per a retornar un user per id
def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cur.fetchone()
       # print("Fetched user:", user)
        cur.close()
        conn.close()
        return user
    except Exception as e:
        print(f"Error reading from database: {e}")
        return None
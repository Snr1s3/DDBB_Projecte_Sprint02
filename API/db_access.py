# Autor: Alba Segura
# Data: 9/10/24

#Importem la funcio db_client de client
from client import db_client

#Funció per a retornar tots els rooms
def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM access")
        access = cur.fetchall()
        cur.close()
        conn.close()
        return access
    except Exception as e:
        print(f"Error reading from database: {e}")
        print(f"Error reading from database: ")
        return []
    
# Function to return access records for a specific user ID
def read_by_user_id(user_id):
    try:
        conn = db_client()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM access WHERE user_id = %s", (user_id,))
        access = cur.fetchall()
        cur.close()
        conn.close()
        return access
    except Exception as e:
        print(f"Error reading from database: {e}")
        return []

# Function to return access records for a specific user ID
def read_by_room_id(room_id):
    try:
        conn = db_client()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM access WHERE room_id = %s", (room_id,))
        access = cur.fetchall()
        cur.close()
        conn.close()
        return access
    except Exception as e:
        print(f"Error reading from database: {e}")
        return []
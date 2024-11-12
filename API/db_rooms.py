# Autor: Alba Segura
# Data: 9/10/24

#Importem la funcio db_client de client
from client import db_client

#Funció per a retornar tots els rooms
def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms")
        rooms = cur.fetchall()
        cur.close()
        conn.close()
        return rooms
    except Exception as e:
        print(f"Error reading from database: {e}")
        print(f"Error reading from database: ")
        return []

#Funció per a retornar un room per id
def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms WHERE id = %s", (id,))
        room = cur.fetchone()
       # print("Fetched room:", room)
        cur.close()
        conn.close()
        return room
    except Exception as e:
        print(f"Error reading from database: {e}")
        return None
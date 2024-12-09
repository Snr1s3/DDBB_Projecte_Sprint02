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
def add_room(name, description, building_name):
    try:
        conn = db_client()
        if conn is None:
            return {"status": -1, "message": "Error connecting to the database"}
        
        cursor = conn.cursor()
        query = """
        INSERT INTO rooms (name, description, building_name)
        VALUES (%s, %s, %s)
        """
        values = (name, description, building_name)
        cursor.execute(query, values)
        conn.commit()
        room_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": 0, "message": "Room added successfully", "room_id": room_id}
    except Exception as e:
        return {"status": -1, "message": f"Error adding room: {e}"}

def updt_room(id, name, description, building_name):
    try:
        conn = db_client()
        if conn is None:
            return {"status": -1, "message": "Error connecting to the database"}
        
        cursor = conn.cursor()
        query = """
        UPDATE rooms SET name = %s, description = %s, building_name = %s
        WHERE id = %s
        """
        values = (name, description, building_name, id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": 0, "message": "Room updated successfully"}
    except Exception as e:
        return {"status": -1, "message": f"Error adding room: {e}"}
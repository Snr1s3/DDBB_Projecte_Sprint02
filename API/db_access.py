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

 # Function to return access records for a specific ID
def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM access WHERE id = %s", (id,))
        access = cur.fetchall()
        cur.close()
        conn.close()
        return access
    except Exception as e:
        print(f"Error reading from database: {e}")
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

# Function to return access records for a specific room ID
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

def add_access(user_id, room_id, entry_time, entry_date, exit_time, exit_date):
    try:
        conn = db_client()
        if conn is None:
            return {"status": -1, "message": "Error connecting to the database"}
        
        cursor = conn.cursor()
        query = """
        INSERT INTO access (user_id, room_id, entry_time, exit_time, entry_date, exit_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (user_id, room_id, entry_time, exit_time, entry_date, exit_date)
        cursor.execute(query, values)
        conn.commit()
        access_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": 0, "message": "Access added successfully", "access_id": access_id}
    except Exception as e:
        return {"status": -1, "message": f"Error adding access: {e}"}

def updt_access(id, user_id, room_id, entry_time, entry_date, exit_time, exit_date):
    try:
        conn = db_client()
        if conn is None:
            return {"status": -1, "message": "Error connecting to the database"}
        
        cursor = conn.cursor()
        query = """
        UPDATE access
        SET user_id = %s, room_id = %s, entry_time = %s, exit_time = %s, entry_date = %s, exit_date = %s
        WHERE id = %s
        """
        values = (user_id, room_id, entry_time, exit_time, entry_date, exit_date, id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": 0, "message": "Access updated successfully"}
    except Exception as e:
        return {"status": -1, "message": f"Error updating access: {e}"}
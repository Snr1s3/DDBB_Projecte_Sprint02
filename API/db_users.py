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

def add_alumn(name, surname, username, DNI, password, email, groups):
    try:
        conn = db_client()
        if conn is None:
            return {"status": -1, "message": "Error connecting to the database"}
        
        cursor = conn.cursor()
        query = """
        INSERT INTO users (name, surname, username, DNI, password, email, groups, rol)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, surname, username, DNI, password, email, groups, 'prof')
        cursor.execute(query, values)
        conn.commit()
        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": 0, "message": "User added successfully", "user_id": user_id}
    except Exception as e:
        return {"status": -1, "message": f"Error adding user: {e}"}

def add_prof(name, surname, username, DNI, password, email, groups):
    try:
        conn = db_client()
        cursor = conn.cursor()
        query = """
        INSERT INTO users (name, surname, username, DNI, password, email, groups, rol)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, surname, username, DNI, password, email, groups, 'prof')
        cursor.execute(query, values)
        conn.commit()
        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": 0, "message": "User added successfully", "user_id": user_id}
    except Exception as e:
        return {"status": -1, "message": f"Error adding userhola: {e}"}

def add_admin(name, surname, username, DNI, password, email, groups):
    try:
        conn = db_client()
        cursor = conn.cursor()
        query = """
        INSERT INTO users (name, surname, username, DNI, password, email, groups, rol)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, surname, username, DNI, password, email, groups, 'admin')
        cursor.execute(query, values)
        conn.commit()
        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": 0, "message": "User added successfully", "user_id": user_id}
    except Exception as e:
        return {"status": -1, "message": f"Error adding userhola: {e}"}

def updt_user(id, name, surname, username, DNI, password, email, groups, rol):
    try:
        conn = db_client()
        cursor = conn.cursor()
        query = """
        UPDATE users
        SET name = %s, surname = %s, username = %s, DNI = %s, password = %s, email = %s, groups = %s, rol = %s
        WHERE id = %s
        """
        values = (name, surname, username, DNI, password, email, groups, rol, id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": 0, "message": "User updated successfully"}
    except Exception as e:
        return {"status": -1, "message": f"Error updating user: {e}"}
def del_user(id):
    try:
        conn = db_client()
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": 0, "message": "User deleted successfully"}
    except Exception as e:
        return {"status": -1, "message": f"Error deleting user: {e}"}
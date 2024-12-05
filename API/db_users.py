# Autor: Alba Segura
# Data: 9/10/24

#Importem la funcio db_client de client
from client import db_client

class UserC(BaseModel):
    name: str
    surname: str
    username: str
    DNI: str
    password: str
    email: str
    group: str
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

def add_alumn(user:UserC):
    try:
        conn = db_client()
        if conn["status"] == -1:
            return conn

        cursor = conn.cursor()
        query = """
        INSERT INTO users (name, surname, username, DNI, password, email, `group`, rol)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (user.name, user.surname, user.username, user.DNI, user.password, user.email, user.group, alumn)
        cursor.execute(query, values)
        conn.commit()
        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": 0, "message": "User added successfully", "user_id": user_id}
    except Exception as e:
        return {"status": -1, "message": f"Error adding user: {e}"}

def add_prof(user: UserC):
    try:
        conn = db_client()
        if conn["status"] == -1:
            return conn

        cursor = conn.cursor()
        query = """
        INSERT INTO users (name, surname, username, DNI, password, email, `group`, rol)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (user.name, user.surname, user.username, user.DNI, user.password, user.email, user.group, prof)
        cursor.execute(query, values)
        conn.commit()
        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"status": 0, "message": "User added successfully", "user_id": user_id}
    except Exception as e:
        print(f"Error reading from database: {e}")
        return None
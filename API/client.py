# Autor: Alba Segura

#Importem la llibreria mysql.connector
import mysql.connector

#Funció per a connectar amb la base de dades
def db_client():
    try:
        dbname = "DDBBPROJ"
        user = "developerUser"
        password = "password"
        host = "localhost"
        port = "3306"
        collation = "utf8mb4_general_ci"
        
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname,
            collation=collation
        )
        
        #print("Connexió a la base de dades correcta")
        return connection
    except Exception as e:
        print(f"Error de connexió: {e}")
        return {"status": -1, "message": f"Error de connexió: {e}"}
# Autor: Alba Segura

# Importem la llibreria datetime
from datetime import datetime

# Funció per a retornar un user
def user_schema(user):
    return {
        "id": user[0],
        "name": user[1],
        "surname": user[2], 
        "username": user[3],
        "DNI": user[4],
        "password": user[5],
        "email": user[6],
        "group": user[7],
        "created_at": user[8].strftime("%Y-%m-%d %H:%M:%S") if isinstance(user[8], datetime) else user[8],
        "updated_at": user[9].strftime("%Y-%m-%d %H:%M:%S") if isinstance(user[9], datetime) else user[9]
    }

# Funció per a retornar tots els users
def users_schema(users):
    return [user_schema(user) for user in users]
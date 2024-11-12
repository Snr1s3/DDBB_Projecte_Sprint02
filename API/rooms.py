# Autor: Alba Segura

# Importem la llibreria datetime
from datetime import datetime

# Funció per a retornar un room
def room_schema(room):
    return {
        "id": room[0],
        "name": room[1],
        "description": room[2], 
        "building_name": room[3],
        "created_at": room[4].strftime("%Y-%m-%d %H:%M:%S") if isinstance(room[4], datetime) else room[4],
        "updated_at": room[5].strftime("%Y-%m-%d %H:%M:%S") if isinstance(room[5], datetime) else room[5]
    }
# Funció per a retornar tots els users
def rooms_schema(rooms):
    return [room_schema(room) for room in rooms]
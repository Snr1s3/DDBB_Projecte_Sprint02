# Autor: Alba Segura

# Importem la llibreria datetime
from datetime import datetime, timedelta, date

# Funció per a retornar un acces
def acces_schema_id(acces):
    return {
        "id": acces["id"],
        "user_id": acces["user_id"],
        "room_id": acces["room_id"],
        "entry_time": str(acces["entry_time"]) if isinstance(acces["entry_time"], timedelta) else acces["entry_time"],
        "exit_time": str(acces["exit_time"]) if isinstance(acces["exit_time"], timedelta) else acces["exit_time"],
        "entry_date": acces["entry_date"].strftime("%Y-%m-%d") if isinstance(acces["entry_date"], date) else acces["entry_date"],
        "exit_date": acces["exit_date"].strftime("%Y-%m-%d") if isinstance(acces["exit_date"], date) else acces["exit_date"],
        "created_at": acces["created_at"].strftime("%Y-%m-%d %H:%M:%S") if isinstance(acces["created_at"], datetime) else acces["created_at"],
        "updated_at": acces["updated_at"].strftime("%Y-%m-%d %H:%M:%S") if isinstance(acces["updated_at"], datetime) else acces["updated_at"]
    }
# Funció per a retornar tots els users
def access_schema_id(access):
    return [acces_schema_id(acces) for acces in access]

# Funció per a retornar un acces
def acces_schema(acces):
    return {
        "id": acces[0],
        "user_id": acces[1],
        "room_id": acces[2],
        "entry_time": str(acces[3]) if isinstance(acces[3], timedelta) else acces[3],
        "exit_time": str(acces[4]) if isinstance(acces[4], timedelta) else acces[4],
        "entry_date": acces[5].strftime("%Y-%m-%d") if isinstance(acces[5], date) else acces[5],
        "exit_date": acces[6].strftime("%Y-%m-%d") if isinstance(acces[6], date) else acces[6],
        "created_at": acces[7].strftime("%Y-%m-%d %H:%M:%S") if isinstance(acces[7], datetime) else acces[7],
        "updated_at": acces[8].strftime("%Y-%m-%d %H:%M:%S") if isinstance(acces[8], datetime) else acces[8]
    }
# Funció per a retornar tots els users
def access_schema(access):
    return [acces_schema(acces) for acces in access]
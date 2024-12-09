# Autor: Alba Segura

# Importem la llibreria datetime
from datetime import datetime, timedelta, date

# Funció per a retornar un acces
def acces_schema_id(acces):
    return {
        "id": acces["id"],
        "user_id": acces["user_id"],
        "room_id": acces["room_id"],
        "entry_time": str(acces["entry_time"]) if acces["entry_time"] is not None else "",
        "exit_time": str(acces["exit_time"]) if acces["exit_time"] is not None else "",
        "entry_date": acces["entry_date"].strftime("%Y-%m-%d") if acces["entry_date"] is not None else "",
        "exit_date": acces["exit_date"].strftime("%Y-%m-%d") if acces["exit_date"] is not None else "",
        "created_at": acces["created_at"].strftime("%Y-%m-%d %H:%M:%S") if acces["created_at"] is not None else "",
        "updated_at": acces["updated_at"].strftime("%Y-%m-%d %H:%M:%S") if acces["updated_at"] is not None else ""
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
        "entry_time": str(acces[3]) if isinstance(acces[3], timedelta) else "",
        "exit_time": str(acces[4]) if isinstance(acces[4], timedelta) else "",
        "entry_date": acces[5].strftime("%Y-%m-%d") if isinstance(acces[5], date) else "",
        "exit_date": acces[6].strftime("%Y-%m-%d") if isinstance(acces[6], date)else "",
        "created_at": acces[7].strftime("%Y-%m-%d %H:%M:%S") if isinstance(acces[7], datetime) else "",
        "updated_at": acces[8].strftime("%Y-%m-%d %H:%M:%S") if isinstance(acces[8], datetime) else ""
    }
# Funció per a retornar tots els users
def access_schema(access):
    return [acces_schema(acces) for acces in access]
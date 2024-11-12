# Autor: Alba Segura

# Importem la llibreria datetime
from datetime import datetime, timedelta, date

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
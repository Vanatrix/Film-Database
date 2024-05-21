import sqlite3 as sql

try:
    with sql.connect("filmflix.db") as cnct:
        cursor = cnct.cursor()
except sql.OperationalError as err:
    print(f"Connection Failure, {err}")
from db_conn import *

def read():
    try:
        cursor.execute("SELECT * FROM tblFilms")
        row = cursor.fetchall()
        for record in row:
            print(record)

    except sql.OperationalError as err:
        print(f"Records not found: {err}")

if __name__ == "__main__":
    read()
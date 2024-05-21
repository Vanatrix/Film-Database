from db_conn import *

def update():
    film_id = int(input("Please enter the ID of the film to be updated: "))
    tbu = input("Which field needs updating? (title, yearReleased, rating, duration genre): ")
    new_val = input(f"Please enter the new {tbu}: ")

    try:
        cursor.execute(f"UPDATE tblFilms SET {tbu} = '{new_val}' WHERE filmID = {film_id}")
        cnct.commit()
        print(f"Record {film_id} updated")

    except sql.OperationalError as err:
        cnct.rollback()
        print(f"Record not updated: {err}")
    
if __name__ == "__main__":
    update()
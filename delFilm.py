from db_conn import *

def delete():
    rec_id = input("Enter ID of the film you want to delete: ")
    try:
        cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {rec_id}")
        cnct.commit()
        print(f"Record {rec_id} deleted")
    
    except sql.OperationalError as err:
        cnct.rollback()
        print(f"Record not found: {err}")
    
if __name__ == "__main__":
    delete()
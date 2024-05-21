from db_conn import *

def add_film():
    film = [] #create record to be added to the db table
    title = input("Enter the film's title: ")
    release = input("Enter the release year: ")
    rating = input("Enter the film's rating: ")
    duration = input("Enter the film's duration: ")
    genre = input("Enter the film's genre': ")
    film = film + [title, release, rating, duration, genre] #add user input to the record

    try:
        cursor.execute("INSERT INTO tblFilms (fitle, release, rating, duration genre) VALUES (?,?,?)", film)
        cnct.commit() #save the db
        print(f"The song {title} has been added to the database")
    
    except sql.OperationalError as err:
        cnct.rollback()
        print(f"Song not added: {err}")

if __name__ == "__main__":
    add_film()
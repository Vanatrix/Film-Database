from seeFilms import read
from db_conn import *

def parameters():
    option = 0
    while option not in ["1", "2", "3", "4", "5"]:
        with open("filmSearch.txt", "r") as menu:
            choices = menu.readlines()
        for line in choices:
            print(line, end="")
        option = input("enter a menu option: ")
        if option not in ["1", "2", "3", "4", "5"]:
            print(f"{option} not applicaple.")
    return option

def exec_search(category, condition):
    try:
        cursor.execute(f"SELECT * FROM tblFilms WHERE {category} = {condition}")
        row = cursor.fetchall()
        for record in row:
            print(record)
    except sql.OperationalError as err:
        print(f"Records not found: {err}")

def film_search():
    loop = True
    while loop:
        selection = parameters()
        if selection == "1":
            read()
        elif selection == "2":
            category = "genre"
            condition = input(f"Pick a condition to filter the {category} field by: ")
            exec_search(category, condition)
        elif selection == "3":
            category = "yearReleased"
            condition = input(f"Pick a condition to filter the {category} field by: ")
            exec_search(category, condition)
        elif selection == "4":
            category = "rating"
            condition = input(f"Pick a condition to filter the {category} field by: ")
            exec_search(category, condition)
        else:
            loop = False


if __name__ == "__main__":
    film_search()
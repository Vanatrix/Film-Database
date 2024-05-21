from addFilm import add_film
from delFilm import delete
from seeFilms import read
from editFilm import update
from searchFilms import *

def menu():
    option = 0
    while option not in ["1", "2", "3", "4", "5", "6"]:
        with open("filmsMenu.txt", "r") as menu:
            choices = menu.readlines()
        for line in choices:
            print(line, end="")
        option = input("enter a menu option: ")
        if option not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{option} not applicaple.")
    return option

def init():
    loop = True
    while loop:
        todo = menu()
        if todo == "1":
            add_film()
        elif todo == "2":
            delete()
        elif todo == "3":
            update()
        elif todo == "4":
            read()
        elif todo == "5":
            film_search()
        else:
            loop = False
    input("Press ENTER to exit")
    return loop

if __name__ == "__main__":
    init()
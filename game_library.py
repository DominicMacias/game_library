#!/usr/bin/python3
# Dominic Macias
# 1/27/2020

''' Editable Database that holds info for multiple games '''

''' Imports '''
import pickle as p

''' Command Functions '''
def add_or_edit():
    print("running add_or_edit()")
    
    
def print_all():
    #print("running print_all()")
    for i in games.keys():
        print("Genre:              ", games[i][0], "\n"
              "Title:              ", games[i][1], "\n"
              "Developer:          ", games[i][2], "\n"
              "Publisher:          ", games[i][3], "\n"
              "Platform:           ", games[i][4], "\n"
              "Release Date:       ", games[i][5], "\n"
              "Rating:             ", games[i][6], "\n"
              "Single/Multi/Either:", games[i][7], "\n"
              "Price:              ", games[i][8], "\n"
              "Beat it?:           ", games[i][9], "\n"
              "Purchase Date:      ", games[i][10], "\n"
              "Notes:              ", games[i][11], "\n"
              "-------------------")

def search():
    print("running search()")

def remove_game():
    print("running remove()")

def save():
    #print("running save()")
    datafile = open("game_lib.pickle", "wb")
    p.dump(games, datafile)
    datafile.close()

def quit():
    #print("running quit()")
    confirm_quit = input("Would you live to save before quitting?(y/n) ")
    if confirm_quit == "y" or confirm_quit == "Y":
        save()

''' File Loader '''
datafile = open("game_lib.pickle", "rb")
games = p.load(datafile)
datafile.close()

''' Main Function '''
keep_going = True
while keep_going:
    print("""
    Welcome to the Game Library
    ---------------------------
    
    MAIN MENU
    1) Add/Edit Game
    2) Print All Games
    3) Search by Title
    4) Remove a Game
    5) Save Database
    
    Q) Quit
    
    """)
    choice = input("What option would you like? ")
    if choice == "1":
        add_or_edit()
    elif choice == "2":
        print_all()
    elif choice == "3":
        search()
    elif choice == "4":
        remove_game()
    elif choice == "5":
        save()

    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
        
    else:
        print("Command not found")

print("Goodbye.")

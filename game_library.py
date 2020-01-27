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
    print("running print_all()")

def search():
    print("running search()")

def remove_game():
    print("running remove()")

def save():
    #print("running save()")
    pickle_file = open("datafile.pickle", "wb")
    pickle.dump(games, pickle_file)
    pickle_file.close()

def quit():
    #print("running quit()")
    confirm_quit = input("Would you live to save before quitting?(y/n) ")
    if confirm_quit == "y" or confirm_quit == "Y":
        print("Saving File...")
        save()

''' File Loader '''
games = {1:['FPS', 'Halo 3', 'Bungie', 'Microsoft', 'Xbox 360', '2007',
            '10', 'either', '30.00', 'Yes', '1/15/2008',
            'Cool game.'}
pickle_file = open("datafile.pickle", "rb")
games = pickle.load(pickle_file)
pickle_file.close()


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

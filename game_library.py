#!/usr/bin/python3
# Dominic Macias
# 1/27/2020

''' Editable Database that holds info for multiple games '''

''' Imports '''
import pickle as p
import dictionary_reset

''' Command Functions '''
def add_or_edit():
    genre = input("What is the genre? ")
    title = input("What is the title of the game? ")
    developer = input("Who developed the game? ")
    publisher = input("Who published it? ")
    platform = input("What platform(s) are able to play this game? ")
    release_date = input("When was this game released (mm/dd/yyyy)? ")
    rating = input("What would you rate this game? ")
    single_or_multi = input("Is this game singleplayer, multiplayer, or either? ")
    price = input("How much does this game cost? ")
    beat_it = input("Have you beaten this game? ")
    purchase_date = input("When did you purchase this game (mm/dd/yyyy)? ")
    notes = input("Any extra notes? ")
    found = False
    for key in games.keys():
        if title == games[key][1]:
            games[key] = [genre, title, developer, publisher, platform, release_date,
                          rating, single_or_multi, price, beat_it, purchase_date,
                          notes]
            found = True
            break
    if not found:
        games[len(games) + 1] = [genre, title, developer, publisher, platform, release_date,
                                 rating, single_or_multi, price, beat_it, purchase_date,
                                 notes]
    
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
              "Price (USD):        ", games[i][8], "\n"
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
try:
    datafile = open("game_lib.pickle", "rb")
    games = p.load(datafile)
    datafile.close()
except:
    #Separate program in the case of a problem with the pickle file.
    dictionary_reset.Reset

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

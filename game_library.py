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
        print_game(games[i])
        
def print_game(game):
    print("Genre:              ", game[0], "\n"
          "Title:              ", game[1], "\n"
          "Developer:          ", game[2], "\n"
          "Publisher:          ", game[3], "\n"
          "Platform:           ", game[4], "\n"
          "Release Date:       ", game[5], "\n"
          "Rating:             ", game[6], "\n"
          "Mode(s)?:           ", game[7], "\n"
          "Price (USD):        ", game[8], "\n"
          "Completed?:         ", game[9], "\n"
          "Purchase Date:      ", game[10], "\n"
          "Notes:              ", game[11], "\n"
          "-------------------")    

def search():
    #print("running search()")
    found = False
    ent_keyword = input("What are you searching for? ")
    if ent_keyword == "Genre" or ent_keyword == "genre":
        search_dictionary(term_answer = "genre", selected_term = 0)
    if ent_keyword == "Title" or ent_keyword == "title":
        search_dictionary(term_answer = "title", selected_term = 1)
    if ent_keyword == "Developer" or ent_keyword == "developer":
        search_dictionary(term_answer = "developer", selected_term = 2)
    if ent_keyword == "Publisher" or ent_keyword == "publisher":
        search_dictionary(term_answer = "publisher", selected_term = 3)
    if ent_keyword == "Platform" or ent_keyword == "platform":
        search_dictionary(term_answer = "platform", selected_term = 4)
    if ent_keyword == "Release Date" or ent_keyword == "release date":
        search_dictionary(term_answer = "release date [mm/dd/yyyy]", selected_term = 5)
    if ent_keyword == "Rating" or ent_keyword == "Rating":
        search_dictionary(term_answer = "rating (out of 10)", selected_term = 6)
    if ent_keyword == "Modes" or ent_keyword == "modes":
        search_dictionary(term_answer = "gamemode(s) [Single/Multi/Either]", selected_term = 7)
    if ent_keyword == "Price" or ent_keyword == "price":
        search_dictionary(term_answer = "price (in USD)", selected_term = 8)
    if ent_keyword == "Completed" or ent_keyword == "completed":
        search_dictionary(term_answer = "completion (Yes/No)", selected_term = 9)
    if ent_keyword == "Purchase Date" or ent_keyword == "purchase date":
        search_dictionary(term_answer = "purchase date [mm/dd/yyyy]", selected_term = 10)


def search_dictionary(term_answer, selected_term = 0):
    term_value = input("Enter " + term_answer + ": ")
    for key in games.keys():
        if term_value in games[key][selected_term]:
            selected_game = key
            print_game(games[selected_game])
            found = True
    
    if not found:
        print("Game Not Found")    

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
    3) Search
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

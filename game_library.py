#!/usr/bin/python3
# Dominic Macias
# 1/27/2020

''' Editable Database that holds info for multiple games '''

''' Imports '''
import pickle as p
import dictionary_reset

''' Command Functions '''
def add_or_edit():
    valid = False
    choose_method = input("Are we adding or editing (Add/Edit) ")
    while not valid:
        if choose_method == "Add" or choose_method == "add":
            new_entry = ask_questions()
            print_game(new_entry)
        if choose_method == "Edit" or choose_method == "edit":
            new_entry = ask_questions(editing = True)
            print_game(new_entry[0])
        
        confirm_changes = input("Is this information correct (y/n)? ")
        if confirm_changes == "Y" or confirm_changes == "y":
            valid = True
    
    if choose_method == "Add" or choose_method == "add":
        for i in range(1,len(games)+2):
            if games[i] not in games.keys():
                games[i] = new_entry
                break  

    if choose_method == "Edit" or choose_method == "edit":
        games[new_entry[1]] = new_entry[0]
    
def ask_questions(editing = False):
    confirm_edit = ""
    while editing and (confirm_edit != "Y" and confirm_edit != "y"):
        print("Original game information:")
        old_info = search_dictionary(term_answer = "title", selected_term = 1)
        confirm_edit = input("Are you sure you'd like to edit this (y/n)? ")

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
    answers = [genre, title, developer, publisher, platform, release_date,
                 rating, single_or_multi, price, beat_it, purchase_date,
                 notes]
    if editing:
        answers = keep_old_changes(answers, old_info)
        return answers, old_info[1]
    return answers
    
def keep_old_changes(entries, old_entries):
    for terms in range(12):
        if entries[terms] == "":
            entries[terms] = old_entries[0][terms]
    return entries
    
def print_all(with_keys = False):
    #print("running print_all()")
    for i in games.keys():
        if with_keys == True:
            print("Key #" + str(i))
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
        print("No games found with this tag")
    
    return games[selected_game], selected_game

def remove_game():
    print_all(with_keys=True)
    selected_key = input("What is the key you would like to delete? ")
    try:
        selected_key = int(selected_key)
        print_game(games[selected_key])
        confirm_deletion = input("Are you sure you want to delete this (Y/N)? ")
        if confirm_deletion == "Y" or confirm_deletion == "y":
            for key in range(1, len(games)+1):
                if key >= selected_key and key != len(games):
                    games[i] = games[i+1]
                if key == len(games):
                    games.pop(key)
    except:
        print("Game Not Found")

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

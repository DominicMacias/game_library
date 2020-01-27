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

def remove():
    print("running remove()")

def save():
    print("running save()")

def quit():
    print("running quit()")

''' Main Function '''
while True:
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
        remove()
    elif choice == "5":
        save()

    elif choice == "Q" or choice == "q":
        quit()

    else:
        print("Command not found")

print("Oh no. Something went horribly wrong.")

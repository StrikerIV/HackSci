import os
import sys
import time
import shutil
from game import startGame
from pynput import keyboard
from colored import fg, bg, attr
#from console import username, password

username1 = ""
password1 = ""

username1Switch = True
confirmPasswordUpdate = True


def clear_line(amount):
    for x in range(0, amount):
        print("\033[A\033[A")


def remove_last_car(string, amount):
    for x in range(0, amount):
        string = string[:-1]

    return string


def add_char(count, char):
    amountOfChar = ''.join([char*count for char in char])
    return amountOfChar


def add_dashes(count):
    amountOfDashes = ''.join([char*count for char in "-"])
    headers = ("+------------%s+" % amountOfDashes + "   ")
    return headers


def welcome_screen():
    print("+---------------------+")
    time.sleep(0.5)
    print("| Welcome to HackSci. |")
    time.sleep(0.5)
    print("+---------------------+")
    time.sleep(1.5)
    print("| 1. New Game         |")
    time.sleep(0.10)
    print("| 2. Credits          |")
    time.sleep(0.10)
    print("+---------------------+\n")
    time.sleep(0.10)

# def update_field():


def new_game():

    global username1
    global password1

    confirm_password = ""

    def create_password():
        global username1
        global password1
        global confirm_password

        password1 = str(input("PASSWORD - "))
        confirm_password = str(input("CONFIRM PASSWORD - "))

        if confirm_password != password1:
            time.sleep(1)
            print("\n%sERR : PASSWORDS DO NOT MATCH%s" % (fg(1), attr(0)))
            time.sleep(2)
            create_password()

    print("+==+ NEW USER REGISTRATION +==+\n")
    username1 = str(input("USERNAME - "))
    create_password()

    print("\n+==+ REGISTRATION COMPLETE +==+")
    time.sleep(1)
    print("\n%sWARNING : Creating a new HackSci game is permanent, you cannot restart.%s" % (
        fg(3), attr(0)))
    time.sleep(1)
    start_game = str(
        input("\nREADY : TYPE %sENTER %sTO CONFIRM - " % (fg(1), attr(0))))

    if start_game.upper() != "ENTER":
        time.sleep(1)
        print("\n%sERR : GAME FAILED TO INITIALIZE%s" % (fg(1), attr(0)))
        time.sleep(2)
        for x in range(0, 6):
            time.sleep(0.5)
            print("\nRESTORING FROM PREVIOUS SESSION SAVE%s" %
                  add_char(x, "."))
            if not x+1 == 6:
                clear_line(2)
            else:
                time.sleep(1)
                print("RESTORED.")
                time.sleep(2)
                for x in range(0, 4):
                    time.sleep(0.5)
                    print("\nINITIALIZING%s" % add_char(x, "."))
                    if not x+1 == 4:
                        clear_line(2)
                    else:
                        time.sleep(1)
                        print("\nDONE.\n")
                        time.sleep(2)
                        return new_game()
    else:
        time.sleep(2)
        startGame(username1, password1)


def main():
    os.system('cls')
    if os.path.exists('data/'):
        shutil.rmtree('data/')
    welcome_screen()
    welcomeInput = str(input(""))
    welcomeInput = welcomeInput.replace(".", "")
    print("")
    if welcomeInput == "1":
        new_game()
    elif welcomeInput == "2":
        print("+---------------+")
        time.sleep(0.10)
        print("|    Credits    |")
        time.sleep(0.10)
        print("+---------------+")
        time.sleep(0.10)
        print("|   Basically   |")
        time.sleep(0.10)
        print("|   Everything  |")
        time.sleep(0.10)
        print("+---------------+")
        time.sleep(0.10)
        print("|  strikeriv /  |")
        time.sleep(0.10)
        print("|    Matthew    |")
        time.sleep(0.10)
        print("+---------------+\n")
        time.sleep(5)
        os.system('cls')
        return main()
    else:
        print("EYO STOP TRYIN TO BREAK THE GAME.")
        time.sleep(1)
        main()


main()

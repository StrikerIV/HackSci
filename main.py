import sys
import time
import keyboard
from console import console
from pynput.keyboard import Key, Listener

username = ""
password = ""
confirmPassword = ""
usernameSwitch = True
confirmPasswordUpdate = True

def clear_line(amount):
    for x in range(0, amount):
        print("\033[A\033[A")

def remove_last_car(string, amount):
    for x in range(0, amount):
        string = string[:-1] 
    
    return string

def add_dashes(count):
    amountOfDashes =  ''.join([char*count for char in "-"])
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
    print("| 2. Help             |")
    time.sleep(0.10)
    print("| 3. Credits          |")
    time.sleep(0.10)
    print("+---------------------+\n")
    time.sleep(0.10)

# def update_field():

def new_game():

    global count
    count = 1

    print("+------------+")
    print("| USERNAME - |")
    print("+------------+")

    def username_update(key):
        global usernameSwitch
        global username
        global count

        if not usernameSwitch: return
        clear_line(3)
        
        #amountOfDashes =  ''.join([char*count for char in "-"])
        #headers = ("+------------%s+" % amountOfDashes)

        if key == Key.backspace:
            count = count - 1
            if count <= 0:
                count = 1

            headers = add_dashes(count)
            actualKey = ''

            username = remove_last_car(username, 1)
            print(headers)
            print("| USERNAME - %s | " % username)
            print(headers)
        elif key == Key.enter: 
            usernameSwitch = False
            print("\n\n\n\n+------------+")
            print("| PASSWORD - |")
            print("+------------+")
            count = 1
            return
        elif key == Key.space:
            actualKey = ' '
            count = count + 1
            headers = add_dashes(count)
            username = username + str(actualKey).replace("'", "")
            print(headers)
            print("| USERNAME - %s |" % username)
            print(headers)
        else:
            username = username + str(key).replace("'", "")
            count = count + 1
            headers = add_dashes(count)
            print(headers)
            print("| USERNAME - %s |" % username)
            print(headers)

    def password_update(key):
        global confirmPasswordUpdate
        global password
        global count

        clear_line(3)
        
        #amountOfDashes =  ''.join([char*count for char in "-"])
        #headers = ("+------------%s+" % amountOfDashes)

        if key == Key.backspace:
            count = count - 1
            if count <= 0:
                count = 1

            headers = add_dashes(count)
            actualKey = ''

            password = remove_last_car(password, 1)
            print(headers)
            print("| PASSWORD - %s | " % password)
            print(headers)
        elif key == Key.enter: 
            Listener.stop(False)
            return console()
        elif key == Key.space:
            actualKey = ' '
            count = count + 1
            headers = add_dashes(count)
            password = password + str(actualKey).replace("'", "")
            print(headers)
            print("| PASSWORD - %s |" % password)
            print(headers)
        else:
            key = "*"
            password = password + str(key).replace("'", "")
            count = count + 1
            headers = add_dashes(count)
            print(headers)
            print("| PASSWORD - %s |" % password)
            print(headers)

    def on_press(key):
        if usernameSwitch:
            username_update(key)
        else:
            password_update(key)
    with Listener(
            on_press=on_press) as listener:
        listener.join()


def main():
    welcome_screen()
    welcomeInput = int(input(""))
    print("")
    if welcomeInput == 1:
        new_game()
    elif welcomeInput == 2:
        print("2")
    elif welcomeInput == 3:
        print("3")
    else:
        print("invalid choice")


main()

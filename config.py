import os
import time

ips = ["192.168.0.1", "68.0.2.5"]

def clear_line(amount):
    for x in range(0, amount):
        print("\033[A\033[A")

def remove_last_car(string, amount):
    for x in range(0, amount):
        string = string[:-1] 
    
    return string

def add_char(count, char):
    amountOfChar =  ''.join([char*count for char in char])
    return amountOfChar

def connect(ip='',end='\n'):
    if not ip:
        return print("enter an ip address to connect to")
    
    if not ip in ips:
        return print("that ip is not valid")
        
    for x in range(0, 5):
        print("\nConnecting%s" % add_char(x, "."))
        if not x+1 == 5: 
            clear_line(2)
        else:
            print("Established connection to %s\n" % ip)
        time.sleep(0.5)

    

def echo(msg='',end='\n'):
    print(msg,end=end)

def python():
    os.system("python")

def bash():
    os.system("bash")

def configHelp():
    print(
"""
== Help Manual ==
Hello, welcome to the help manual!\n
\n
Lets get started on creating your interpreter (console)!\n
\n
First step is to configurate it to your own preference!\n
To go this, go to main.py and change the variables in the configuration.\n
! DONT CHANGE THE COMPILER'S CODE UNLESS YOU KNOW WHAT YOU ARE DOING!\n
\n
Next step is to start creating the commands!\n
Go to config.py and delete all the premade functions in it if you want.\n
The commands are just functions in python and the parameters are function parameters!\n
\n
Have fun!\n
Don't forget to share your interpreter in the comments below, hope to see what you guys make!
"""
)
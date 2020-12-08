import random as rand
import time
import os

ips = ["192.168.0.1", "68.0.2.5"]
created_computer_ips = []

def rand_key(p): 
    key1 = "" 
    for i in range(p): 
        temp = str(rand.randint(0, 1)) 
        key1 += temp 
          
    return(key1)  
    
def clear_line(amount):
    for x in range(0, amount):
        print("\033[A\033[A")
        return x


def remove_last_car(string, amount):
    for x in range(0, amount):
        string = string[:-1]
        return x

    return string


def add_char(count, char):
    amountOfChar = ''.join([char*count for char in char])
    return amountOfChar


def createComputer(ip):
    if ip in created_computer_ips: return
    print("hello u made it!")
    created_computer_ips.append(ip)
    


createComputer("192.168.0.1")
print("1")
createComputer("67.246.453.3")
print("2")
createComputer("192.168.0.1")
print("3")

def connect(ip='', end='\n'):
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

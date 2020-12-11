from console import variables
from pynput import keyboard
import random as rand
import shutil
import time
import os

ips = variables.ips
created_computer_ips = []


def randBinary(p):
    key1 = ""
    counter = 0
    while True:
        if counter == p:
            break
        temp = str(rand.randint(0, 1))
        key1 += temp
        counter += 1

    return(key1)

def clear_lines(amount):
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


# def cat(operator='', file_name=''):
#     if operator == '>':
#         def on_press():

#         with keyboard.Listener(
#                 on_press=on_press) as listener:
#             listener.join()


def ls():
    curr_dir = variables.current_directory
    current_computer = variables.current_computer
    files = os.listdir("data/%s%s" % (current_computer, curr_dir))
    for file in files:
        print(file)
    print("")


def mkdir(dir=''):
    if not dir:
        return print("The syntax of the command is incorrect.\n")
    curr_dir = variables.current_directory
    current_computer = variables.current_computer
    os.mkdir("data/%s%s/%s" % (current_computer, curr_dir, dir))


def cp(file='', path=''):
    if not file:
        return print("The syntax of the command is incorrect.\n")

    home_comp = variables.home_computer
    curr_comp = variables.current_computer
    curr_dir = variables.current_directory

    file = "data/%s%s/%s" % (curr_comp, curr_dir, file)

    if not os.path.isfile(file):
        return print("The system cannot find the file specified.\n")
    if not path:
        path = ("data/%s/home" % home_comp)

    shutil.copy(file, path)


def cd(path=''):
    print(path)
    createComputer(variables.current_computer)
    curr_path = variables.current_directory
    curr_path = curr_path.split("/")
    if not path:
        return print(variables.current_directory)
    if path == "..":
        curr_path = curr_path[:-1]
        curr_path = "/".join(curr_path)
        variables.current_directory = curr_path
        return

    navPath = ("data/%s%s/%s" %
               (variables.current_computer, "/".join(curr_path), path))

    if not os.path.isdir(navPath):
        return print("The system cannot find the path specfied.\n")

    curr_path = "".join(curr_path).replace(" ", "")
    print("")
    variables.current_directory = ("%s/%s" % (curr_path, path))


def createComputer(ip=''):
    if ip in created_computer_ips:
        return

    directory = ('data/%s' % ip)

    if not os.path.exists(directory):
        os.makedirs(directory)
        os.makedirs('%s/bin' % directory)
        os.makedirs('%s/home' % directory)
        os.makedirs('%s/logs' % directory)
        os.makedirs('%s/os' % directory)

    os_config = open("%s/os/os-config.sys" % directory, "w+")
    os_config.write(randBinary(1000))

    boot_cfg = open("%s/os/boot-cfg.dll" % directory, "w+")
    boot_cfg.write(randBinary(350))

    network_sys = open("%s/os/network.sys" % directory, "w+")
    network_sys.write(randBinary(125))

    server_sys = open("%s/os/server.sys" % directory, "w+")
    server_sys.write(randBinary(500))


def connect(ip=''):

    if not ip:
        return print("Enter an ip address to connect to.\n")

    if not ip in ips:
        return print("Can't find a server with that ip address.\n")

    createComputer(ip)

    for x in range(0, 5):
        time.sleep(0.5)
        print("\nConnecting%s" % add_char(x, "."))
        if not x+1 == 5:
            clear_lines(2)
        else:
            time.sleep(1)

    print("\nEstablished connection to %s\n" % ip)

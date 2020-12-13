from utils import variables
from pynput import keyboard
import random as rand
import shutil
import time
import os




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
    createComputer(variables.current_computer)
    curr_path = variables.current_directory
    curr_path = curr_path.split("/")

    if path == "ports": return print("The system cannot find the file specified.\n")
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

    if ip in variables.created_computers_ips:
        return

    directory = ('data/%s' % ip)

    if not os.path.exists(directory):
        os.makedirs(directory)
        os.makedirs('%s/bin' % directory)
        os.makedirs('%s/home' % directory)
        os.makedirs('%s/logs' % directory)
        os.makedirs('%s/os' % directory)
        os.makedirs('%s/ports' % directory)

    os_config = open("%s/os/os-config.sys" % directory, "w+")
    os_config.write(randBinary(1000))

    boot_cfg = open("%s/os/boot-cfg.dll" % directory, "w+")
    boot_cfg.write(randBinary(350))

    network_sys = open("%s/os/network.sys" % directory, "w+")
    network_sys.write(randBinary(125))

    server_sys = open("%s/os/server.sys" % directory, "w+")
    server_sys.write(randBinary(500))

    ports = open("%s/ports/ports.txt" % directory, "w+")

    flags = 1

    if variables.has_ftpBounce:
        flags = flags << 2
    if variables.has_sshCrack:
        flags = flags << 3
    if variables.has_SQLWormOverflow:
        flags = flags << 4
    if variables.has_SMTPMailOverflow:
        flags = flags << 5
    if variables.has_HTTPS:
        flags = flags << 6

    ports.write(str(flags))

    variables.created_computers_ips.append(ip)

def scan():
    ips = variables.ips

    if variables.current_computer in variables.scanned_computers:
        return print("You've already scanned this computer, there's no need to again.")

    for x in range(0, 5):
        time.sleep(0.5)
        print("\nScanning%s" % add_char(x, "."))
        if not x+1 == 5:
            clear_lines(2)
        else:
            time.sleep(1)

    scanned_ip = ips.pop(rand.randint(0, len(ips)))
    print("\nScanned network on ip %s and found -\n\n%s\n" % (variables.current_computer, scanned_ip))

    variables.discovered_ips.append(scanned_ip)
    variables.scanned_computers.append(variables.current_computer) 


def connect(ip=''):

    if not ip:
        return print("Enter an ip address to connect to.\n")

    if not ip in variables.discovered_ips:
        return print("Can't find a server with that ip address.\n")

    createComputer(ip)

    for x in range(0, 5):
        time.sleep(0.5)
        print("\nConnecting%s" % add_char(x, "."))
        if not x+1 == 5:
            clear_lines(2)
        else:
            time.sleep(1)

    variables.current_computer = ip
    variables.current_directory = ""
    print("\nEstablished connection to %s." % ip)

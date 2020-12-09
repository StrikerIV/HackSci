import random as rand
import console
import time
import os

ips = console.discoveredIps()
created_computer_ips = []


def randBinary(p):
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
    if ip in created_computer_ips:
        return

    directory = ('data/%s/os' % ip)

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
    print(ips)
    # if not ip:
    #     return print("enter an ip address to connect to")

    # if not ip in ips:
    #     return print("that ip is not valid")

    # for x in range(0, 5):
    #     print("\nConnecting%s" % add_char(x, "."))
    #     if not x+1 == 5:
    #         clear_line(2)
    #     else:
    #         print("Established connection to %s\n" % ip)
    #     time.sleep(0.5)

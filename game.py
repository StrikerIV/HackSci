import random as rand
from console import console, username, password
import time
import os

ip_addresses = []
maxIps = 100

homeIp = ""


def s(timeToSleep):
    time.sleep(timeToSleep)

def clear_line(amount):
    for x in range(0, amount):
        print("\033[A\033[A")

def add_char(count, char):
    amountOfChar = ''.join([char*count for char in char])
    return amountOfChar


def add_dashes(count):
    amountOfDashes = ''.join([char*count for char in "-"])
    headers = ("+------------%s+" % amountOfDashes + "   ")
    return headers

def create_ips():
    counter = 0
    while True:
        if counter == maxIps:
            break
        int1 = rand.randint(0, 255)
        int2 = rand.randint(0, 168)
        int3 = rand.randint(0, 200)
        int4 = rand.randint(0, 100)

        ip_addr = ("%s.%s.%s.%s" % (int1, int2, int3, int4))
        if ip_addr in ip_addresses:
            return print("already in ip_addresses: %s" % ip_addr)
        ip_addresses.append(ip_addr)
        counter += 1


def terminal_loading(username, ip):
    os.system('cls')
    print("\nHackSci Kernal V.1.69 Wednesday, October 20, 1971 PTB V.1.42.0 %s@%s" %
          (username, ip))
    s(0.5)
    print("vm_page_bootstrap: 42069 free pages and 593 wires pages")
    s(0.15)
    print("submap [0xffff] mapped, kernal text [0xffff - 9xffff]")
    s(0.15)
    print("leak detection subnet enabled")
    s(0.15)
    print("HackSciAPICPU: ProcessorId=1 Initialized")
    s(0.15)
    print("HackSciAPICPU: ProcessorId=2 Initialized")
    s(0.15)
    print("HackSciAPICPU: ProcessorId=2 Initialized")
    s(0.15)
    print("HackSciAPICPU: ProcessorId=2 Initialized")
    s(0.15)
    print("calling policy be_careful for SafteyHandler")
    s(0.15)
    print("Security policy loaded: (SafteyHandler")
    s(0.15)
    print("calling policy VPN for sshs_network")
    s(0.15)
    print("Security policy loaded: (sshs_network)")
    s(0.15)
    print("addition dependencies required - Quarantine policy, masks flag")
    s(0.15)
    for x in range(0, 4):
        time.sleep(0.5)
        print("\nPiping into sshs_network%s" % add_char(x, "."))
        if not x+1 == 4:
            clear_line(2)
        else:
            time.sleep(1)
            print("Done.\n")
            time.sleep(2)
    print("Framework HackSci loaded.")
    s(0.25)
    print("Copyright (c) 1975, 1991, 2020 ")
    s(0.25)
    print("AP Computer Science of SSHS. All rights not reserved.\n")
    time.sleep(2)
    print("Loading os-config.sys : System Initialized")
    s(0.25)
    print("Loading boot-cfg.dll : Boot-Config Loaded")
    s(0.25)
    print("Loading network.sys : Network System Loaded")
    s(0.25)
    print("Loading server.sys : NVIDIA Graphics Loaded\n")
    time.sleep(2)
    for x in range(0, 5):
        time.sleep(0.5)
        print("\nReady. Restarting now%s" % add_char(x, "."))
        if not x+1 == 4:
            clear_line(2)
        else:
            time.sleep(2)
            os.system('cls')
            console(username)

    time.sleep(3)



def startGame(username1, password1):
    create_ips()
    username.value(username1)
    password.value(password1)
    homeIp = rand.choice(ip_addresses)
    terminal_loading(username1, homeIp),


#startGame("strikeriv", "test")

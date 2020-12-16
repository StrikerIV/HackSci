from utils import variables
import numpy as np
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

    if path == "ports":
        return print("The system cannot find the file specified.\n")
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

    os_config = open("%s/os/os-config.sys" % directory, "w+")
    os_config.write(randBinary(1000))

    boot_cfg = open("%s/os/boot-cfg.dll" % directory, "w+")
    boot_cfg.write(randBinary(350))

    network_sys = open("%s/os/network.sys" % directory, "w+")
    network_sys.write(randBinary(125))

    server_sys = open("%s/os/server.sys" % directory, "w+")
    server_sys.write(randBinary(500))

    firewall = False
    proxy = False

    ftp = False
    ssh = False
    sql = False
    smtp = False
    https = False

    if variables.has_firewall:
        firewall = True
    if variables.has_proxy:
        proxy = True

    if variables.has_ftpBounce:
        ftp = True
    if variables.has_sshCrack:
        ssh = True
    if variables.has_SQLWormOverflow:
        sql = True
    if variables.has_SMTPMailOverflow:
        smtp = True
    if variables.has_HTTPSTrojan:
        https = True

    variables.computer_data_ips.append(ip)
    variables.computer_data_ports.append(
        [firewall, proxy, "BREAK", ftp, ssh, sql, smtp, https])
    variables.computer_admin.append(False)


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
    print("\nScanned network on ip %s and found -\n\n%s\n" %
          (variables.current_computer, scanned_ip))

    variables.discovered_ips.append(scanned_ip)
    variables.scanned_computers.append(variables.current_computer)

    return scanned_ip


def probe():
    for x in range(0, 5):
        time.sleep(0.5)
        print("\nProbing%s" % add_char(x, "."))
        if not x+1 == 5:
            clear_lines(2)
        else:
            time.sleep(1)

    print("Probed computer %s for ports - \n" % variables.current_computer)
    time.sleep(0.5)

    index = 0

    loggingStuff = ["| Firewall - %s", "| Proxy - %s", "BREAK",
                    "| FTP: 21 - %s", "| SSH: 22 - %s", "| SQL: 1433 - %s", "| SMTP: 465 - %s", "| HTTPS: 443 - %s"]

    print("+----------+")
    time.sleep(0.25)

    for port in variables.computer_data_ports[0]:
        if port == "BREAK":
            print("+----------+")
            time.sleep(0.05)
        else:
            if port:
                port = "Closed"
            else:
                port = "Open"

            print(loggingStuff[index] % port)
            time.sleep(0.05)

        index += 1

    print("+----------+\n")


def ftpbounce(port=''):
    port = str(port)
    if not port == "21":
        return print("FTP does not run on this port.\n")

    if variables.computer_data_ports[0][3]:
        for x in range(0, 5):
            time.sleep(0.5)
            print("\nBouncing%s" % add_char(x, "."))
            if not x+1 == 5:
                clear_lines(2)
            else:
                time.sleep(1)

        print("\nSuccessfully bounced FTP on port 21.\n")
        variables.computer_data_ports[0][3] = False
    else:
        print("This port is already hacked.\n")


def sshcrack(port=''):
    if not port == "22":
        return print("SSH does not run on this port.\n")

    if variables.computer_data_ports[0][4]:
        for x in range(0, 5):
            time.sleep(0.5)
            print("\nCracking%s" % add_char(x, "."))
            if not x+1 == 5:
                clear_lines(2)
            else:
                time.sleep(1)

        print("\nSuccessfully cracked SSH on port 21.\n")
        variables.computer_data_ports[0][4] = False
    else:
        print("This port is already hacked.\n")


def sqlwormoverflow(port=''):
    if not port == "1433":
        return print("SSH does not run on this port.\n")

    if variables.computer_data_ports[0][5]:
        for x in range(0, 5):
            time.sleep(0.5)
            print("\nOverflowing%s" % add_char(x, "."))
            if not x+1 == 5:
                clear_lines(2)
            else:
                time.sleep(1)

        print("\nSuccessfully overflowed SQL on port 1433 with worm.\n")
        variables.computer_data_ports[0][5] = False
    else:
        print("This port is already hacked.\n")


def smtpmailoverflow(port=''):
    if not port == "465":
        return print("SMTP does not run on this port.\n")

    if variables.computer_data_ports[0][6]:
        for x in range(0, 5):
            time.sleep(0.5)
            print("\nOverflowing%s" % add_char(x, "."))
            if not x+1 == 5:
                clear_lines(2)
            else:
                time.sleep(1)

        print("\nSuccessfully overflowed SMTP protocol on port 465.\n")
        variables.computer_data_ports[0][6] = False
    else:
        print("This port is already hacked.\n")


def httpstrojan(port=''):
    if not port == "443":
        return print("HTTPS does not run on this port.\n")

    if variables.computer_data_ports[0][7]:
        for x in range(0, 5):
            time.sleep(0.5)
            print("\nOverflowing%s" % add_char(x, "."))
            if not x+1 == 5:
                clear_lines(2)
            else:
                time.sleep(1)

        print("\nSuccessfully inserted trojan on port 443 and hacked port.\n")
        variables.computer_data_ports[0][7] = False
    else:
        print("This port is already hacked.\n")


def porthack():
    unhacked = 0
    for port in variables.computer_data_ports[0]:
        if port:
            if not port == "BREAK":
                unhacked += 1

    if unhacked > 0:
        return print("All ports are not hacked, therefor porthack cannot proceed.\n")

    for x in range(0, 5):
        time.sleep(0.5)
        print("\nHacking%s" % add_char(x, "."))
        if not x+1 == 5:
            clear_lines(2)
        else:
            time.sleep(1)

    print("\nSuccessfully hacked computer %s. You are now administrator of this computer.\n" %
          variables.current_computer)

    variables.hacked_computers.append(variables.current_computer)
    hacked = variables.total_hacked
    hacked += 1

    if hacked == 5:
        variables.has_sshCrack = True
    elif hacked == 10:
        variables.has_ftpBounce = True
    elif hacked == 15:
        variables.has_SQLWormOverflow = True
    elif hacked == 20:
        variables.has_SMTPMailOverflow = True
    elif hacked == 25:
        variables.has_HTTPSTrojan = True
    elif hacked == 50:
        print("AWE U BEAT THE GAME!!!!!!!!!!\nUnfortuently if you keep going we'll run out of ips and it will crash, so go ahead and crash the game to end the game.\n\n:)")


def help():
    print("\n+==+ Help - Page 1 +==+\n")
    time.sleep(0.25)
    print("connect - Connect to a remote computer with specified ip address.\n")
    print("cd - Navigates to current directory.")
    print("help - This command!\n")
    print("ls - Lists files and directories in current directory.")
    print("mkdir - Makes directory with given path and folder name.")
    print("probe - Probe the computers firewall.\n")
    print("ftpbounce - Sends a denial of service attack to the specified FTP port.")
    print("scan - Scans the current computers network to find connected computers.\n")
    print("+==+   +==+\n")
    return


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

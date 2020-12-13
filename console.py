from inspect import signature as s, isfunction as f
from json import loads as parse, dumps as stringify
from colored import fg, bg, attr
from utils import variables, ips
import random as rand
import config
import time
import os


class error:
    syntax_error = "'{}' is not a valid command.\n"
    name_error = "'{}' is not defined."
    type_error = "The supplied parameters for '{}' are the wrong type.\n"
    invalid_parameter_error = "{required_params} required parameters required and {optional_params} optional parameters needed but {params_given} given."


i = 0

user_color = "white"
console_color = "white"

username = variables.username
password = variables.password

current_directory = variables.current_directory

ip = variables.current_computer

maxIps = 100

pointer = ("%s%s@%s%s: %s~%s %s$%s" % (fg(2), username, variables.current_computer,
                                       fg(15), fg(4), variables.current_directory, fg(4), attr(0)))
pointer_color = "white"
error_color = fg(1)

##################################################
##################################################
##################################################


def e(c):
    exec('global i; i = %s' % c)
    global i
    return i


def clear_lines(amount):
    for x in range(0, amount):
        print("\033[A\033[A")


def add_char(count, char):
    amountOfChar = ''.join([char*count for char in char])
    return amountOfChar


def create_ips():
    counter = 0
    ip_addresses = []
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

    variables.ips = ip_addresses

##################################################
##################################################
##################################################


def starting_text():
    print("Welcome to HackSci. You're in a framework called, well, HackSci, created by Microsocks.\n")
    time.sleep(3)
    print("This is a beta program contracted by the U.S. Government as a tool for other countries.")
    time.sleep(4)
    print("Unfortuently for them some hackers got their hands on it, and here we are.\n")
    time.sleep(4)
    print("Sorry, forgot to introduce myself. The name's Jenkins. I'll help you out with the basics.")
    time.sleep(4)
    print("At any time you can type %shelp%s to view commands." %
          (fg(4), attr(0)))
    time.sleep(2)
    print("Go ahead and do it now. I'll be waiting.\n")
    time.sleep(1.5)


def getInput(p):
    u = str(input("%s " % p))
    return u


def tryHelp():
    sinput = getInput(pointer)
    if sinput == "help":
        print("\n+==+ Help - Page 1 +==+\n")
        time.sleep(0.25)
        print("connect - Connect to a remote computer with specified ip address\n")
        print("help - This command!\n")
        # print("nmap - Look up a computers approximent location.")
        print("probe - Probe the computers firewall.\n")
        print("ftpdos - Sends a denial of service attack to the specified FTP port.")
        print("scan - Scans the current computers network to find connected computers.\n")
        print("+==+   +==+\n")
        return
    else:
        print("\nBro, cmon. You're wasting my time. Try again.\n")
        time.sleep(1)
        tryHelp()


def firstScan():
    sinput = getInput(pointer)
    if sinput == "scan":
        return e("config.scan()")
    else:
        print("EYO STOP TRYIN TO BREAK THE TUTORIAL unless u mistyped it all good ;)\n")
        time.sleep(1)
        firstScan()


def firstConnect(ip):
    connectt = getInput(pointer)
    connectt = connectt.split()
    if connectt[0] == "connect":
        e("config.connect" + '("' + str(ip) + '")')
    else:
        print("EYO STOP TRYIN TO BREAK THE TUTORIAL unless u mistyped it all good ;\n)")
        time.sleep(1)
        firstConnect(ip)


def firstProbe():
    input = getInput(pointer)
    if input == "probe":
        for x in range(0, 4):
            time.sleep(0.5)
            print("\nProbing%s" % add_char(x, "."))
            if not x+1 == 4:
                clear_lines(2)
            else:
                time.sleep(1)

        print("\nProbed computer 192.168.0.1 for ports -\n")
        time.sleep(2)
        print("+-------------------+")
        time.sleep(0.05)
        print("| Firewall - Open   |")
        time.sleep(0.05)
        print("|   Proxy - Open    |")
        time.sleep(0.05)
        print("+-------------------+")
        time.sleep(0.05)
        print("| FTP: 21 - Closed  |")
        time.sleep(0.05)
        print("| SSH: 22 - Open    |")
        time.sleep(0.05)
        print("| SQL: 1433 - Open  |")
        time.sleep(0.05)
        print("| SMTP: 465 - Open  |")
        time.sleep(0.05)
        print("| HTTPS: 443 - Open |")
        time.sleep(0.05)
        print("+-------------------+\n")
    else:
        print("EYO STOP TRYIN TO BREAK THE TUTORIAL unless u mistyped it all good ;)\n")
        time.sleep(1)
        firstProbe()


def console(username):
    #create_ips()
    global pointer
    username = username
    pointer = ("%s%s@%s%s: %s~%s %s$%s" % (fg(2), username, variables.current_computer,
                                           fg(15), fg(4), variables.current_directory, fg(4), attr(0)))
    starting_text()
    tryHelp()
    time.sleep(2)
    print("The help menu displays the basic commands. As you progress, you will gather more tools, but they all follow the same command format.")
    time.sleep(4)
    print("That should be all for now. Go ahead and use %sscan%s to scan your network for another computer.\n" % (fg(4), attr(0)))
    time.sleep(2)
    #############
    scanned_ip = firstScan()
    time.sleep(1)
    print("Nice! You just found your first ip address! Go ahead and connect to the computer with %sconnect%s, plus the ip address obviously.\n" % (fg(4), attr(0)))
    time.sleep(2)
    firstConnect(scanned_ip)
    pointer = ("%s%s@%s%s: %s~%s %s$%s" % (fg(2), username, variables.current_computer,
                                           fg(15), fg(4), variables.current_directory, fg(4), attr(0)))
    print("\nNow you're connected to the computer, but we don't have access. Let's fix that.")
    time.sleep(2.5)
    print("But wait, you ask, isn't this illegal? Yep! But if you're up to the task, you'll never get caught.\n")
    time.sleep(4)
    print("We're going to %sprobe%s the computer to scan its ports. We can then hack the ports to gain administrative access to the computer." % (fg(4), attr(0)))
    time.sleep(4)
    print("Go ahead and do that now.\n")
    time.sleep(2)
    firstProbe()
    print("Looks like this server only has port 21 closed, which means all we need to do is crack that port.")
    time.sleep(3)
    print("To do this, run %sftpbounce%s, plus the port.\n" % (fg(4), attr(0)))
    #config.createComputer("192.168.0.1")

    while True:
        current_directory = variables.current_directory
        updateIp = variables.current_computer
        pointer = ("%s%s@%s%s: %s~%s %s$%s" % (fg(2), username, updateIp,
                                               fg(15), fg(4), current_directory, fg(4), attr(0)))
        x = input(pointer + " ")
        if x in variables.blacklistedCommands:
            return
        if x.strip() != "":
            y = x.split(" ")
            c = x.split(" ")[0]
            del(y[0])
            for a in y:
                y[y.index(a)] = '"'+a+'"'
            y = ','.join(y)
            sig = ''
            prm = [0, 0]
            try:
                if f(e("config." + c)):
                    sig = s(e("config." + x.split(" ")[0]))
                    for key in list(dict(sig.parameters).keys()):
                        if str(dict(sig.parameters)[key]).startswith("{}=".format(key)):
                            prm[1] += 1
                        else:
                            prm[0] += 1
                    if (len(y.split(",")) == prm[0] or y.split(",") == ['']) or len(y.split(",")) <= (prm[0] + prm[1]):
                        if not y == "":
                            e("config." + c + "(" + y + ")")
                        else:
                            try:
                                e("config." + c + "()")
                            except Exception as error:
                                print("<[function] {}> - %s".format(c) % error)
                    else:
                        print(error_color + error.invalid_parameter_error.format(
                            required_params=prm[0], optional_params=prm[1], params_given=len(y.split(","))))

                else:
                    raise AttributeError
            except (AttributeError, SyntaxError):
                print(error_color + error.syntax_error.format(x))


#console("strikeriv")

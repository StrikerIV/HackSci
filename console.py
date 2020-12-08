from inspect import signature as s, isfunction as f
from json import loads as parse, dumps as stringify
from colored import fg, bg, attr
import random as rand
import config
import time
import os

class Username:
    def __init__(self):
        self.username = 'null'
    
    def __str__(self):
        return self.username

    def value(self, username):
        assert isinstance(username, str)
        self.username = username

class Password:
    def __init__(self):
        self.password = ''
    
    def __str__(self):
        return self.password

    def value(self, password):
        assert isinstance(password, str)
        self.password = password


class error:
    syntax_error = "'{}' is not a valid command."
    name_error = "'{}' is not defined."
    type_error = "wrong type for '{}'"
    invalid_parameter_error = "{required_params} required parameters required and {optional_params} optional parameters needed but {params_given} given."

ip_addresses = []
maxIps = 100
i = 0

user_color = "white"
console_color = "white"

username = Username()
password = Password()

ip = "192.168.0.1"

pointer = ("%s%s@%s%s:%s-$%s" % (fg(2), username, ip, fg(15), fg(4), attr(0)))
pointer_color = "white"

error_color = "red"

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
    print("At any time you can type %shelp%s to view commands." % (fg(4), attr(0)))
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
        #print("nmap - Look up a computers approximent location.")
        print("probe - Probe the computers firewall.\n")
        print("ftpdos - Sends a denial of service attack to the specified FTP port.")
        print("scan - Scans the current computers network to find connected computers.\n")
        return
    else:
        print("\nBro, cmon. You're wasting my time. Try again.\n")
        time.sleep(1)
        tryHelp()

def firstScan():
    sinput = getInput(pointer)
    if sinput == "scan":
        for x in range(0, 5):
            time.sleep(0.5)
            print("\nScanning%s" % add_char(x, "."))
            if not x+1 == 5:
                clear_lines(2)
            else:
                time.sleep(1)

        scanned_ip = ip_addresses.pop(rand.randint(0, len(ip_addresses)))
        print("Scanned network on ip 192.168.0.1 and found -\n\n%s\n" % scanned_ip)
        return scanned_ip
    else:
        print("Hey, I won't help you if you keep this up.")
        time.sleep(1)
        firstScan()

def firstConnect(ip):
    e("config.connect" + '("' + ip + '")')

def console(username):
    global pointer
    username = username
    pointer = ("%s%s@%s%s:%s-$%s" % (fg(2), username, ip, fg(15), fg(4), attr(0)))
    create_ips()
    # starting_text()
    # tryHelp()
    #print("The help menu displays the basic commands. As you progress, you will gather more tools, but they all follow the same command format.")
    # time.sleep(4)
    # print("That should be all for now. Go ahead and use %sscan%s to scan you network for another computer.\n" % (fg(4), attr(0)))
    # scanned_ip = firstScan()
    # time.sleep(1)
    # print("Nice! You just found your first ip address! Go ahead and connect to the computer with %sconnect%s, plus the ip address obviously." %(fg(4), attr(0)))
    scanned_ip = "192.168.0.2"
    firstConnect(scanned_ip)
    while True:
        x = input(pointer + " ")
        if x.strip() != "":
            y = x.split(" ")
            c = x.split(" ")[0]
            del(y[0])
            for a in y:
                y[y.index(a)] = '"'+a+'"'
            y = ','.join(y)
            # print(y)
            #y = '"' + x + '"'
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
                        try:
                            if not y == "":
                                print("here")
                                print(y)
                                e("config." + c + "(" + y + ")")
                                print("config." + c + "(" + y + ")")
                            else:
                                try:
                                    print("here1")
                                    print("config." + c + "()")
                                    e("config." + c + "()")
                                except:
                                    print("here2")
                                    print("<[function] {}>".format(c))
                        except TypeError:
                            print(error_color + error.type_error.format(x))
                        except NameError:
                            print(error_color + error.name_error.format(x))
                    else:
                        print(error_color + error.invalid_parameter_error.format(
                            required_params=prm[0], optional_params=prm[1], params_given=len(y.split(","))))

                else:
                    raise AttributeError
            except (AttributeError, SyntaxError):
                print(error_color + error.syntax_error.format(x))

console("strikeriv")
from inspect import signature as s, isfunction as f
from json import loads as parse, dumps as stringify
from colored import fg, bg, attr
import random as rand
import config

# -- Configuration (Settings) -- #
user_color = "white"
console_color = "white"

class Language:
    def __init__(self):
        self.language = 'en-US'
    
    def __str__(self):
        return self.language

    def change(self, lang):
        assert isinstance(lang, str)
        self.language = lang

language = Language()

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


username = Username()
password = Password()

ip = "192.168.0.1"

pointer = ("%s%s@%s%s:%s-$%s" % (fg(2), username, ip, fg(15), fg(4), attr(0)))
pointer_color = "white"

# {} is the command given by the user


class error:
    syntax_error = "'{}' is not a valid command."
    name_error = "'{}' is not defined."
    type_error = "wrong type for '{}'"
    invalid_parameter_error = "{required_params} required parameters required and {optional_params} optional parameters needed but {params_given} given."


error_color = "red"

do_help_command = True  # use the built-in help command?
help_command = "help"

version = "1.0.0"  # what is the version of your language?
language_name = "ExampleLanguage"
author = "ExamplePerson"

clear_command = ["clear", "clr"]  # you can have aliases to the command


##################################################
##################################################
##################################################

ip_addresses = []
maxIps = 100


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


create_ips()

colors = {
    "white": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "purple": "\033[35",
    "cyan": "\033[36m",
    "orange": "\033[33m"
}

i = 0

def e(c):
    exec('global i; i = %s' % c)
    global i
    return i


try:
    user_color = colors[user_color]
    console_color = colors[console_color]
    pointer_color = colors[pointer_color]
    error_color = colors[error_color]
except:
    print("\033[31mInvalid colors in configuration.\033[0m")

help = '== Help ==\nFor help with a command, type help [command]'


def console():
    #print("Welcome to HackSci. ")
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
                                e("config." + c + "(" + y + ")")
                            else:
                                try:
                                    e("config." + c + "()")
                                except:
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

#console()
import random as rand

class ips:
    def __init__(self):
        counter = 0
        ip_addresses = []
        maxIps = 100
        while True:
            if counter == maxIps:
                break
            int1 = rand.randint(0, 255)
            int2 = rand.randint(0, 168)
            int3 = rand.randint(0, 200)
            int4 = rand.randint(0, 100)

            ip_addr = ("%s.%s.%s.%s" % (int1, int2, int3, int4))
            if ip_addr in ip_addresses:
                return
            ip_addresses.append(ip_addr)
            counter += 1
            ips_s = str(" ".join(ip_addresses))
            self.ips = ips_s

    def __str__(self):
        return str(self.ips)


class variables:
    username = "root"
    password = "roota"

    home_computer = "192.168.0.1"
    current_computer = "192.168.0.1"
    current_directory = ""
    
    ips = []


import socket 
from IPy import IP


def scan_port(addr, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((addr, port))
        try:
            banner = get_banner(s)
            print(f"Port {port} is open : {banner}")
        except:
            print(f"Port {port} is open")
    except:
        pass#print(f"Port {port} is closed")


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan(target):
    converted_ip = check_ip(target)
    print(f"Scanning Target : {converted_ip}")
    for port in range(78, 81):
        scan_port(converted_ip, port)


def get_banner(s):
    return s.recv(1024)

Targets = input("Enter yout Targets/s (split with ',' if multiple target's) : ")
if ',' in Targets:
    for ip_add in Targets.split(','):
        scan(ip_add)
else:
    scan(Targets)

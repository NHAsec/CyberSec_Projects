import sys, socket, pyfiglet

ascii_banner = pyfiglet.figlet_format("Python 4 Pentesters \nPort Scanner")
print(ascii_banner)

ip = input('Enter ip to scan: ')

open_ports = []

ports = range(1,1024)

def probe_port(ip, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        print(f"Trying port: {port}")
        r = sock.connect_ex((ip,port))
        if r == 0:
            print(f"Port {port} is open")
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

for port in ports:
    sys.stdout.flush()
    response = probe_port(ip,port)
    if response == 0:
        open_ports.append(port)

if open_ports:
    print("Open ports are: ")
    print (sorted(open_ports,reverse=True))
else:
    print("Looks like no ports are open :(")

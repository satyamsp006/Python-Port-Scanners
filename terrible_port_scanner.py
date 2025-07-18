import socket
import sys
host = sys.argv[1]
ip = socket.gethostbyname(host)
print(f"Scanning {ip}")
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()

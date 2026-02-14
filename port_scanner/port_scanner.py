import socket
import time

target = "192.168.129.219"
ports = [21, 22, 23, 25, 53, 80, 135, 443, 445, 3389]

print(f"Scanning common ports on {target}...\n")

start_time = time.time()

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    if s.connect_ex((target, port)) == 0:
        print(f"[OPEN] Port {port}")

    s.close()

end_time = time.time()

print(f"\nScan finished in {round(end_time - start_time, 2)} seconds")
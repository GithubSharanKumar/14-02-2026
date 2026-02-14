import socket

domain = "google.com"


ip = socket.gethostbyname(domain)
print(f"Domain {domain} has IP: {ip}")

try:
    reverse_domain = socket.gethostbyaddr(ip)
    print(f"IP {ip} resolves to domain: {reverse_domain[0]}")
except socket.herror:
    print(f"IP {ip} does not have a reverse DNS entry")
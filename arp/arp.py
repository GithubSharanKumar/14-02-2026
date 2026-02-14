from scapy.all import ARP, Ether, srp

# 1. Set the target network range
target_ip = "192.168.129.0/24"  # Your local network range

# 2. Create ARP request packet
arp_request = ARP(pdst=target_ip)

# 3. Create a broadcast Ethernet frame (send to all devices)
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

# 4. Combine ARP request with broadcast frame
arp_request_broadcast = broadcast/arp_request

# 5. Send the packet and capture responses
answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

# 6. Print results
print("IP Address\t\tMAC Address")
print("-----------------------------------")
for sent, received in answered_list:
    print(f"{received.psrc}\t\t{received.hwsrc}")
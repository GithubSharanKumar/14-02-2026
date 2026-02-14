from scapy.all import sniff

def process_packet(packet):
    with open("packets.txt", "a") as f:
        f.write(packet.summary() + "\n")

sniff(count=10, prn=process_packet)
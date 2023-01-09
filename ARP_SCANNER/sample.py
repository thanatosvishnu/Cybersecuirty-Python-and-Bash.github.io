import scapy.all as scapy

def scan(ip):
    apr =scapy.arping(ip)
    print(apr)

scan("10.0.2.1/24")
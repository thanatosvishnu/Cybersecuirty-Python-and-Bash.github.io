#!/usr/bin/env python

#Using function to change mac address

import subprocess
import platform
from optparse import OptionParser
import re

my_system = platform.uname()
def get_arguments():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="user_input", help="Interface to change the mac address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    return parser.parse_args()

def mac_changer(user_input, mac):
    if user_input == "eth0" or user_input == "wlan0":
        subprocess.call(f"ifconfig {user_input} down", shell=True)
        if len(mac) == 17: 
            subprocess.call(f"ifconfig {user_input} hw ether {mac}", shell=True)
            subprocess.call(f"ifconfig {user_input} up", shell=True)
            
        else:
            subprocess.call(f"ifconfig {user_input} up", shell=True)
            print("Please specfiy a valid mac address")
    else:
        subprocess.call(f"ifconfig {user_input} up", shell=True)
        print("Please specfiy a valid input")

def current_mac(user_input):
    ifconfig_result = subprocess.check_output(['ifconfig', user_input]).decode(encoding='utf-8', errors='strict')

    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("MAC address cloud not be changed")


(options, argument) = get_arguments()
current_mac_address = current_mac(options.user_input)
if current_mac_address:
    print(f"current mac : {current_mac_address}")
    mac_changer(options.user_input, options.mac)
    current_mac_address = current_mac(options.user_input)

    if current_mac_address == options.mac:
        print(f"MAC address successfully changed to {options.mac} ")
    else:
        print("Mac address cloud not be changed")
else:
    print("please specfiy a valid interface")
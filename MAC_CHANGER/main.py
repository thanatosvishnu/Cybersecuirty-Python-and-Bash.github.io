#!/usr/bin/env python

#Simple mac changer 

import subprocess
import platform

my_system = platform.uname()


print(""" 
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||M |||A |||C |||       |||C |||H |||A |||N |||G |||E |||R ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|

""")

success = True
print(f"It looks like your using {my_system.system}")
while success:
    
    user_input = input("Interface(eth0/wlan0) > ")

    if user_input == "eth0" or user_input == "wlan0":
        subprocess.call(f"ifconfig {user_input} down", shell=True)
        done = True
        while done:
            mac = input(f"NEW MAC FOR {user_input} > ")
            if len(mac) == 17: 
                subprocess.call(f"ifconfig {user_input} hw ether {mac}", shell=True)
                subprocess.call(f"ifconfig {user_input} up", shell=True)
                print(f"MAC address successfully changed to {mac} ")
                done = False
                success = False
            else:
                print("Invalid input or mac address length is not correct")
    else:
        print("Invalid input")


#! /bin/bash

echo "
██████╗░██╗███╗░░██╗░██████╗░  ░██████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░
██╔══██╗██║████╗░██║██╔════╝░  ██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗
██████╔╝██║██╔██╗██║██║░░██╗░  ╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░██████╔╝
██╔═══╝░██║██║╚████║██║░░╚██╗  ░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░██╔═══╝░
██║░░░░░██║██║░╚███║╚██████╔╝  ██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░░░░
╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░░░░"


#First we get the network portion from the user and store it in a variable
read -p "Enter the subnet or network portion: " SUBNET

#Then we use the for loop with "seq" sequence command to generate numbers from FIRST to LAST in steps of INCREMENT
for ip in $(seq 1 10); do
#we try to ping the give ip if its up or not 
	ping -c 1 $SUBNET.$ip
done

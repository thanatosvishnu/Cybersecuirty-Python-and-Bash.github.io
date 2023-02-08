#! /bin/bash

#Getting info from users
read -p "Enter the length for your password: " PASS

read -p "Enter the algorithm you want to use: " ALG

read -p "How many passwords do want to generate: " GEN

#using for loop to generate "N" number of password based on the user given info
for len in $(seq 1 $GEN); 
do 
#Here we used "openssl" command to generate the password and used the pipe fliter to get the output from openssl and give it as input for the "cut" command to cut the password based the user given length which they want
 
	openssl rand -$ALG 48 | cut -c1-$PASS
	
done

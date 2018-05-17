#!/usr/bin/env python3
#Gerald Chikukwa
#Date 5/18/2018
#networkscope.py - The script detects the network scope of the the machine that's running it.
# The script displays the Host Computer information like IP Address, Subnet Mask and Gateway
# It also displays IP Addresses on the network with a status(Inactive or live)

import subprocess   #Import subprocess module 
import os           #Import os module 
import socket       #Import socket module
import netifaces    #Import netifaces module
import sys          #Import sys module 

def main():
 with open(os.devnull, "wb") as subprocess.PIPE:
    
    print("  ")
    print(" Host Computer : ")
    print("  ")

    #Gets the IP Address, Subnet Mask and Gateway for the host
    for i in netifaces.interfaces():
        try:
            print(" IP Address: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
            print(" Subnet Mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
            print(" Gateway: ", netifaces.gateways()['default'][netifaces.AF_INET][0])
            print(" ")
            
        except:pass
        
            
    print(" Hosts on the Network :")
    print("  ")
    
    #Gets the IP Addresses of hosts on the network  and display if they are live hosts or inactive hosts
    for n in range(1, 20):
            ip_address ="192.168.1.{0}".format(n)
            result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip_address],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
            if result:
                    print(ip_address,"  Inactive Host")
                    
            else:
                    print(ip_address,"  live Host")
                                         

if __name__ == '__main__': main()

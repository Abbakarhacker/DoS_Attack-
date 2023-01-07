import socket

    

h_name = socket.gethostname()

IP_addres = socket.gethostbyname(h_name)

print("Host Name is:" + h_name)

print("Computer IP Address is:" + IP_addres)


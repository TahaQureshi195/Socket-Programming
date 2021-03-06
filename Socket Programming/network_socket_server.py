"""
Author : Taha Qureshi

Title : Socket Programming
A socket is used in networking to send data from source to destination
i.e , Between two end points

                                        *** SERVER MACHINE ***
"""


import socket

# SRV_ADDR = "192.168.1.131"
# SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Sucessfully Created a socket !")
s.bind(('localhost' , 9999))  # port range (0-65535)

# I'm giving Local host as I using same machine for server as well as client

s.listen(1) #Here one is you just wait for "1" connection/device

print("Server started! Waiting for connections...")

connection, address = s.accept()

print('Client connected with address:', address)

connection.send(bytes("Welcome to the Tee.Q Network !" ,"utf-8"))

connection.close()

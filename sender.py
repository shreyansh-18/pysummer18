#!/usr/bin/python

import socket
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	msg =raw_input="Write  message- "
	x.sendto(msg,("192.168.122.1",9999))
 	print x.recvfrom(1000)



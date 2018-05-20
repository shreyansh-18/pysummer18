#!/usr/bin/python

import socket
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("127.0.0.1",9999))

while 1+1:
	data=x.recvfrom(1000)
	print "data from client : ",data[0]
	rply=raw_input("Please reply - ")
	x.sendto(rply, data[1])
j

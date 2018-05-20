#!/usr/bin/python

import socket

rec_ip="192.168.42.108"
myport=9999

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((rec_ip,myport))

while True:
	s.recvfrom(1000)

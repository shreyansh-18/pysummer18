#!/usr/bin/python

import time
import requests
import webbrowser
from bs4 import BeautifulSoap
option='''
"Enter your choice -"
"1. To search every word of string."
"2. To search image for every word of string."
"3. To print URL's of page 1 of google search."
"4. To print current time and date of system."
"5. To open default web browser."
"6. To give network IP's."
"7. To enter domain and check its owner."
'''
print option
n=raw_input()
if n=='1':
	search_data=raw_input("Enter data -")
	final_data=search_data.strip()
	#removes space leading and trailing
	done_data=final_data.split()
	#splitting each word by space
	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)

elif n=='2':
	search_data=raw_input("Enter data -")
	final_data=search_data.strip()
	#removes space leading and trailing
	done_data=final_data.split()
	#splitting each word by space
	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i+'tbm=isch')

elif n=='3':
	search=raw_input("Enter data")
	page=requests.get('https://www.google.com/search?q='+search)
	soup=BeautifulSoup(page.content,'html.parser')
	url=[]	
	url.append(soup.find_all('a'))
	for i in url:
		print i

elif n=='4':
		print time.asctime()
	
elif n=='5':
		webbrowser.open_new_tab('https://')

else
	print ("Wrong Entry!!")

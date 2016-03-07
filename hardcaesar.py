#!/usr/bin/env python
# -*- coding: utf-8 -*-
from colorama import Fore, Back, Style
print """
#####################
#   Caesar Cipher   #
#       v1.0        #
#      h4yuc3       #
#####################
"""
def getValue():
	return raw_input('Enter for decrypt : ')

def Solver(text):
	
	solved = ''
	Key = 0
	while Key < 26:
		Key=Key+1
		for char in text:
			if char.isalpha():
				num = ord(char)
				num += Key
				
				if char.isupper():
					if num > ord('Z'):
						num -= 26
					elif num < ord('A'):
						num += 26
				elif char.islower():
					if num > ord('z'):
						num -= 26
					elif num < ord('a'):
						num += 26
				solved += chr(num)
			else:
				solved += char
		solved += (' [%s] \n' %Key)	
	return solved
		
text = getValue()	

with open('list.txt', 'r') as infile:
	data = infile.read()

status = ''
theword = []
my_list = data.splitlines()	
line = len(my_list) - 1
turn = -1

while turn < line:
	turn +=1
	wordLine = Solver(text).splitlines()
	for kelime in wordLine:
		if my_list[turn] in kelime:
			print (Fore.RED + kelime)
		#else:
			#print (Fore.GREEN + kelime)
	

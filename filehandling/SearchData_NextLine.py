'''
This script is used to analysis the log message from sql server, This script will check any message
start with Msg and then print the next line. Please see the example below, 

Msg 208, Level 16, State 1, Line 3
Invalid object name 'Patients'.
'''

import re

File = raw_input("Please enter the file name:")

fh = open(File)
T = 0
for element in fh:
	#use strip to break the whole file into line
	line = element.strip()
	if T == 1:
		print line
		T = 0
	elif re.match('^Msg', line):
	#or use if line.startswith('Msg'):
		print line
		# use T to control the printing of the next line
		T = 1



"""
This program includes two parts:
Part 1 is to stream line the process from reading, processing and analysis file from a folder
Part 2 is to demo how to connect SQL servers with pyodbc driver
""" 

#Part one: read and process files with python
import os
import glob
import re
import json

#==============================================================================
#           Process all related files and sort out the information
#==============================================================================

path = raw_input('Please enter your file directory:')
read_files =  glob.glob(os.path.join(path, '*.arr')) 

##print the package name and save it into a file
'''
with open("File_Info.txt", "wb") as outfile:
	for f in read_files:
		f.replace(path+'\\', '').replace('.arr', '').replace('.PRC', '').replace('dbo.', '')
		outfile.write(f.replace(path+'\\', '').replace('.arr', '').replace('.PRC', '').replace('dbo.', '') + "\n")
outfile.close()	
'''

with open("File_Info.json", "wb") as outfile:
	for f in read_files:
		lst = list()
		source = None
		T = 0  #use this to deal with table right behind of 'From' or 'Join' but in next line
		for line in open(f, 'r'):
			line = line.strip()

			if line.startswith('<Source>'): 
				source = line.replace('<Source>', '').replace('</Source>', '')
			
			groups = line.split()
			if T == 1 and len(groups)>0:
				table = groups[0].replace('[','').replace(']','').replace('(','').replace(')','')
				if table.find('dbo.') >= 0:
					table = table[table.find('dbo.')+4:len(table)]
				if not table in lst and table != '':
					lst.append(table)
				T = 0
			else:
				#print type(groups)
				for i in range(len(groups)):
				#find if elements in groups are FROM or JOIN
					if (groups[i] == 'FROM' or groups[i] == 'JOIN'): 
						try:
							table = groups[i+1].replace('[','').replace(']','').replace('(','').replace(')','')
							if table.find('dbo.') >= 0:
								table = table[table.find('dbo.')+4:len(table)]
							if not table in lst:
								lst.append(table)
						except:
							T = 1
							break
		#write into a json file. The reason tha I don't use txt file is because there is a list which can not write into a txt file
		json.dump([f.replace(path+'\\', '').replace('.arr', '') ,source, lst], outfile)
		outfile.write('\n')

#==============================================================================
#                       Insert data into sql server database
#==============================================================================
import sys
import pyodbc
import ast
###create a connection with pyodbc 
connection_str =    """
Driver={SQL Server Native Client 11.0};
Server=localhost;
Database=test;
Trusted_Connection=yes;
"""
db_connection = pyodbc.connect(connection_str)
db_connection.autocommit = True  #very import, otherwise you will not see the result
db_cursor = db_connection.cursor()

###create a table
sql_command =   """
CREATE TABLE File_Info(
PackageName VARCHAR(100),
SourceDB VARCHAR(50),
TableList VARCHAR(MAX));
"""

try:
	db_cursor.execute(sql_command)

except pyodbc.ProgrammingError:
	print("command fail to execute.")

###insert data into the table
fl = open('File_Info.JSON').readlines()

for f in fl:
	#python can not read null
	f = f.replace('null', 'None')
	f = ast.literal_eval(f)
	col1 = f[0]
	col2 = f[1]
	col3 = str(f[2])[1:-1]
	sql_command = ("INSERT INTO File_Info (PackageName, SourceDB, TableList) VALUES (?,?,?)")	
	Values = [col1, col2, col3] 
	db_cursor.execute(sql_command,Values) 
	
###query the result

sql_command =   """
SELECT PackageName, SourceDB, TableList FROM File_Info
"""
try:
	db_cursor.execute(sql_command)
except pyodbc.ProgrammingError:
	print("command fail to execute.")

row = db_cursor.fetchone()
while row:
	##We only select two column so your index should not great than 1
    print 'The load package %s was loaded from %s, the source tables are %s.' %(str(row[0]),str(row[1]),str(row[2]))  
    row = db_cursor.fetchone()	

#close cursor and connection	
db_cursor.close()
del db_cursor
db_connection.close()

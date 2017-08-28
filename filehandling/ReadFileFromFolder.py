"""
This program includes two parts:
Part 1 is to stream line the process from reading, processing and analysis file from a folder
Part 2 is to demo how to connect SQL servers with pyodbc driver
""" 

#Part one: read and process files with python
import os
import glob
import re

###Read all files into a file


path = r'SourceDirectoryPath'
read_files =  glob.glob(os.path.join(path, '*.txt'))
#print read_files
###switch the directory so the newly generated file will not be saved in the directory of the source files 
path1 = r'DestinationDirectoryPath'
os.chdir(path1)
with open("myFilesReadLine.txt", "w") as outfile:   #python 2.7 use "wb"
    for f in read_files:
        
        if (f.find('EP_') >= 0 and f.find('_EP_') < 0) or f.find('EH_') >= 0 or f.find('Visits_') >= 0:
            print(f)
        ##to read the whole file, please use the code below
        #with open(f, "rb") as infile:  
        #outfile.write(infile.read())
        ##to read line by line, please use the code below
            for line in open(f, 'r'):
                line = line.strip()
                outfile.write(line + "\n")
outfile.close()

###process the file, find your interested tables and put them into a list.
excludedtables = ['']
lst = list()
fh = open("myFilesReadLine.txt", 'r')  #python 2.7 use "rb" instead of "r"
for line in fh:
    groups = line.strip().split()
    #print type(groups)
    for group in groups:
        group = group.replace('([UpdateDateTime])', '').replace(')', '').replace("'", '')
        #find group contains '.dbo.' and 'Bar' but not 'jsplit'
        if group.find('.dbo.') > 1 and group.find('jsplit') < 1 and group.find('#') < 0:
            table = group[group.find('.dbo.')+5:len(group)]
            if not table in lst and len(table) > 2 and table not in excludedtables:
                
                lst.append(table)
        if group.find('([UpdateDateTime])') > 1:
            
            if group.find('.dbo.') > 1 :
                table = group[group.find('.dbo.')+5:len(group)]
                if not table in lst and len(table) > 2 and table not in excludedtables:
                    print(table)
                    lst.append(table)
            else:
                table = group[0:group.find('([UpdateDateTime]')-1]
            #append unique table in the list
                if table not in lst and len(table) > 2 and table not in excludedtables:
                    lst.append(table)
###print out the list of table	
print(len(lst))
lst_sorted = sorted(lst)

with open("Tables.txt", 'w') as JuniperFocusTables:
    for tbl in lst_sorted:
        JuniperFocusTables.write(tbl + "\n")

'''
###return back to the source file and find which files contains any of those tables
#read_files =  glob.glob(os.path.join(path, 'Visits*.arr'))
for f in read_files:
	for line in open(f, 'r'):
		line = line.strip()
		for tbl in lst:
			if line.find(tbl)> 1:
				print f.replace(path+'\\', ''), tbl
'''				
##Part two: connect python to SQL server				
'''				
##=================================================================
###connect to sql server with pyodbc. you need to download pyodbc driver		
###you may also try pymssql	
import sys
import pyodbc
connection_str =    """
Driver={SQL Server Native Client 11.0};
Server=localhost;
Database=test;
Trusted_Connection=yes;
"""
db_connection = pyodbc.connect(connection_str)
#db_connection.autocommit = True
db_cursor = db_connection.cursor()
sql_command =   """
SELECT PatientIDNew, Address2 FROM T
"""
try:
	db_cursor.execute(sql_command)
except pyodbc.ProgrammingError:
	print("command fail to execute.")

row = db_cursor.fetchone()
while row:
	##We only select two column so your index should not great than 1
    print str(row[0]) + " " + str(row[1])   
    row = db_cursor.fetchone()			
db_cursor.close()
del db_cursor
db_connection.close()
'''
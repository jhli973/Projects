'''
This script is used to analysis a package, This script will check any duplicate scripts for creating an index.
.

IF NOT EXISTS (SELECT * FROM dbo.sysindexes WHERE name = N'Idx_UpdateDateTime' and id = object_id(N'[TableName]'))
 CREATE  INDEX [Idx_UpdateDateTime] ON [dbo].[TableName]([UpdateDateTime]) ON [PRIMARY]
 
 
 --TableName
IF EXISTS (SELECT * FROM sys.objects WHERE name = N'TableName')
 BEGIN 
   IF NOT EXISTS (SELECT * FROM sysindexes WHERE name = N'Idx_UpdateDateTime' and id = object_id(N'[TableName]'))
   CREATE INDEX [Idx_UpdateDateTime] ON [dbo].[TableName] ([UpdateDateTime] ASC) ON [PRIMARY] 
 END 
'''

#D:\MeditechLoadUpdateIndex\MeditechLoadUpdateIndexes.arr
#import re
#import os

#File = "OriginalFile.txt"
File = "FinalFile.txt"

fh = open(File)

lst = {}
for element in fh:
	#use strip to break the whole file into line
	lines = element.strip()
	if lines.find('Idx_UpdateDateTime') > 0 and lines.find("object_id") >0:
		lines = lines.split(' ')
		#pick the last element and subset the string by '[' and ']'
		k = lines[-1][lines[-1].find("[")+1 : lines[-1].find("]")]
		
		#count the total numbers
		if k in lst:
			lst[k] += 1
		else:
			lst[k] = 1


#print duplicate tables

for k,v in lst.items():
	if v > 1:
		print "Table %s has %s copy." %(k ,v)
	else:
		print "No duplicate find for %s" %k
	
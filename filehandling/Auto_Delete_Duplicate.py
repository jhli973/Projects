'''
This script is used to analysis a package, This script will check any duplicate scripts for creating an index.
if there is, then will generate a new file without duplication named FinalFile.

IF NOT EXISTS (SELECT * FROM dbo.sysindexes WHERE name = N'UpdateDateTime' and id = object_id(N'[YourTableName]'))
 CREATE  INDEX [UpdateDateTime] ON [dbo].[YourTableName]([UpdateDateTime]) ON [PRIMARY]
 
 
 --YourTableName
IF EXISTS (SELECT * FROM sys.objects WHERE name = N'YourTableName')
 BEGIN 
   IF NOT EXISTS (SELECT * FROM sysindexes WHERE name = N'UpdateDateTime' and id = object_id(N'[YourTableName]'))
   CREATE INDEX [UpdateDateTime] ON [dbo].[YourTableName] ([UpdateDateTime] ASC) ON [PRIMARY] 
 END 
'''

#D:\MeditechLoadUpdateIndex\MeditechLoadUpdateIndexes.arr
import re
import os

File = "OriginalFile.txt"

fh = open(File)

lst = {}
for element in fh:
	#use strip to break the whole file into line
	lines = element.strip()
	if lines.find('UpdateDateTime') > 0 and lines.find("object_id") >0:
		lines = lines.split(' ')
		#pick the last element and subset the string by '[' and ']'
		k = lines[-1][lines[-1].find("[")+1 : lines[-1].find("]")]
		
		#count the total numbers of scripts for each table
		if k in lst:
			lst[k] += 1
		else:
			lst[k] = 1


#print duplicate tables
dup_lst = {k:v for k, v in lst.items() if v >1}		

print 'start print dlu_list'
for k,v in dup_lst.items(): 
	print k, v

#generate a copy (FinalFile.txt) without duplicate	
fh1 = open('OriginalFile.txt')
fh1_lst = fh1.readlines()

print "The length of original fh1_lst is %d." %len(fh1_lst)
for item in fh1_lst:
	for k,v in dup_lst.items():
		if v > 1 and item.find('UpdateDateTime') > 0 and k in item:
			dup_lst[k] -= 1
			id = fh1_lst.index(item)
			id_lst =[]
			for i in xrange(id-1, 0, -1):
				if fh1_lst[i].strip() != '':
					id_lst.append(i)
				else:
					break
			for i in xrange(id, len(fh1_lst), 1):
				if fh1_lst[i].strip() != '':
					id_lst.append(i)
				else:
					break
			#remove all lines of the script for creating the duplicate index	
			for j in id_lst:
				try:
					#note: the index will not be change because we delete a item each time
					del fh1_lst[id_lst[0]]
				except:
					print  "something wrong"

print "The length of fh1_lst after deleting duplicate is %d." %len(fh1_lst)
	
with open('FinalFile.txt', 'w') as finalfile:
	for item in fh1_lst:
		finalfile.write(item)						

print 'start print dlu_list'
for k,v in dup_lst.items(): 
	print k, v		

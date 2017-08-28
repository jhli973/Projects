
'''
We have houdreds of client specific folders which hold packages files.
Our mission is to check if two specific packages were created for each clients
This program is to find the specified files from any folder and return a 
ordered dictionary of the foldername(ClientName):filename
'''


#Part one: read and process files with python
import os
import glob
import re

###1. give a path, don't add backslash to the end
path = raw_input("Please enteryour directory, otherwise use the default one.")
if path == '':
	path = r'C:\Users\jli\Documents\Visual Studio 2012\Projects\Juniper2013\Juniper.root\JuniperLoad_1.0.649\Clients'

###2. read all subfolder
#change the path to working directory
os.chdir(path)
##read only the subfolder name 
#print [name for name in os.listdir(".") if os.path.isdir(name)]
subdirectories = [name for name in os.listdir(".") if os.path.isdir(name)]
##read the absolute subfolder name 
#subdirectories = [os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name)]

###3. select subfolder contains 'EP_Patients_Load.arr' or file == 'EP_Insurance_Load.arr' file and 
# put the subfolder and filename into dictionary tbl_dict
tbl_dict  = {}
dir_dict = {}
for subdir in subdirectories:
	##cancatenate the path aand subdir
	abssubdir = path + '\\' + subdir
	#set the 
	os.chdir(abssubdir)
	files  = os.listdir(".")  #return a list
	##the following returns the a list of the absolute directory
	#files =  glob.glob(os.path.join(subdir, '*.arr'))
	for file in files:
		#print file
		if file == 'EP_Patients_Load.arr' or file == 'EP_Insurance_Load.arr':
			#print subdir, file
			##insert into a dictionary
			tbl_dict.setdefault(subdir, []).append(file)
			dir_dict.setdefault(abssubdir, []).append(file)
			'''
			if subdir in tbl_dict: 
				tbl_dict[subdir].append([file]) # see error AttributeError: 'str' object has no attribute 'append'
			else:
				tbl_dict[subdir] = file
            '''
#print the sorted dictionary according to the keys				
for key, value in sorted(tbl_dict.items()):
	print key, value


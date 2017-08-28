#Part one: read and process files with python
import os

path = r'DirectoryName'
os.chdir(path)
###switch the directory so the newly generated file will not be saved in the directory of the source files 
    
for filename in os.listdir(".") :
    if filename.endswith("_New.sql"):
        os.rename(filename, filename[:-8] + ".sql")
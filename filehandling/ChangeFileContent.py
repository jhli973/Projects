
"""
This function changes an old string found in all
files inside a folder into a new string 
"""

"""
takes three arguments: 
oldstr: the old content to be replaced (in string format)
newstr: the new string (in string format)
fileextension: example 'sql'

An example: ChangeFileContent('[OldDatabaseName]', 'NewDatabaseName', 'sql')
"""
import os

def ChangeContent(oldstr, newstr, fileextension):

    try:
        if fileextension:
            fileextension = '*.' + fileextension
    except:
        print("Please enter you file extension, for exampel 'sql'.")
    

    ###Read all files with '.sql' extension
    path = os.getcwd()
    read_files =  glob.glob(os.path.join(path, '*.sql'))

    for f in read_files:
        
        with open(f, 'r+') as openfile:
            fh = open(f, 'r')
            for line in fh.readlines():
                line = line.replace(oldstr, newstr)
                openfile.write(line)

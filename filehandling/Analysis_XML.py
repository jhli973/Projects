
#Import xml.etree.ElementTree

import xml.tree.ElementTree as ET


fname = "Wiki_Hadoop.xml"



#tree = ET.parse(fname)
#root = tree.getroot()
parser = ET.XMLParser(encoding='utf-8')	
root = ET.parse(fname, parser=parser)

print "Print root information \n"

print root.tag
print "\n"
print root.attrib

print "\n"
print "Print child information \n"

for child in root:
	print child.tag
	#print child.attrib

print "\n"
print "print page information \n"	

for page in root.findall('page'):
	if page: print "Good"
	title = page.find('title').text
	print title
	


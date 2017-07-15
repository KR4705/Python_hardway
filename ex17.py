from sys import argv # argument from console 
from os.path import exists # ?? 

script, from_file, to_file = argv #unpacking to variables
print "copying from %s to %s" %(from_file,to_file)
indata =  open(from_file).read()  #indata = the data in the from_file
#when you wirte open.read it auto closes the opened file. 'handy stuff'

# print "the input file is %d bytes long" % len(indata)
#exists is method we imported from os.path 
#it takes <type "str"> as input and outputs
#whether the file of that "path" exists. 

# print "Does the output file exists? %r" % exists(to_file)
# print "Hit CTRL+C(^C) to exit , RETURN to continue"
# raw_input()

# to file opened with write mode
open(to_file, 'w').write(indata)
print "Done."


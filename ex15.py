# ex15.py
from sys import argv

script,filename = argv # unpacks the scriptname to var script
# and the argument filename to filename
txt = open(filename) # open(<type "str">) gives <type "file">
# from pydoc: open(name[, mode[, buffering]]) -> file object

print "Here's your file: %s" %filename 
print txt.read() 


# read() is a method for <type "file"> which gives the 
# text in the file as <type "str">
# similar to above but taking raw_input()


print "type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print type(txt_again.read()) 
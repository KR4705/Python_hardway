# ex13.py
from sys import argv #imports a certain module from python module set
# argv : argument variable 

script,first,second,third = argv # this "unpacks" the arguments 
# take whatever is in argv "unpack" it and assign it to the variables to left
# in order.

# script,first,second,raw_input("third?") = argv
# cant assign argv unpacking to a function call only to variables. 

# takes arguments.string

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# type("string") = <type 'str'> this itself is of type <type 'type'>
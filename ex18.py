#this one like the argv
#takes multiple arguments
def print_two(*args):
	arg1, arg2 = args # unpacking args into arg1 and arg2 
	#args is like a tuple
	print type(args) 
	print "arg1: %r, arg2: %r"%(arg1,arg2)

#we can also do like this
def print_two_again(arg1,arg2):
	print type(arg1)#this type is dependent on the input given
	print "arg1: %r, arg2: %r"%(arg1,arg2)

#just takes one argument
def print_one(arg1):
	print "arg1: %r"%arg1

def print_none():
	print "I got nothing"


print_two("rs","pk")
print_two_again("rs","pk")
print_one("sreeramdas")
print_none()

def add(*args):
	a , b  = args
	print "Adding %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "Subtracting %d - %d" % (a,b)
	return a-b

def multiply(a,b):
	print "multipying %d * %d" %(a,b)
	return a*b

def divide(a,b):
	print "dividing %d / %d" %(a,b)
	return a/b


age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "age : %d , height : %d , weight : %d , iq : %d " % (age,height,weight,iq)

print "Here is a puzzle"

what = add(age,subtract(height,multiply(weight,divide(iq,2))))
# note the inside out nature of calculating the function inside a function.

# what = age + height - weight * iq / 2

print "That becomes", what ,"can you do it by hand?"



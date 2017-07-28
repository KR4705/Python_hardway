ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "wait there are not 10 things in that list lets fix that"

stuff = ten_things.split(' ')
more_stuff = ["day","night","song","firsbee","corn","banana","girl","boy"]

while not len(stuff) == 10 :
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "there are %d items now" %len(stuff)

print "there we go" , stuff

print "lets do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

# nothing much to learn in this except pop() 

print dir(stuff)
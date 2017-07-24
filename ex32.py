the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'dimes']

for number in the_count:
	print "This is count:%d" %number

for fruit in fruits:
	print "A fruit of type: %s" %fruit

for i in change:
	print "i got %r" %i

# elements = []

# for i in range(0,6):
# 	print "adding %d to the list." % i
# 	elements.append(i)
elements = range(0,6)


# the below functions work in place 
# elements.reverse()
# elements.sort()
# elements.remove(2) 
# elements.extend(iterable)  
# elements *= 2 
# multipying list by int implies list values repeating themselves


# the below return values
# element.count(0) 
# elements.index(value) returns first occurance of value 
# elements[0:-1] 
# elements.pop()  
# elements.append(value) insert at the end
# elements.insert(value,index) inserts x before index
# elements.remove(value) removes first occurance of value


for i in elements:
	print "element was: %d" %i
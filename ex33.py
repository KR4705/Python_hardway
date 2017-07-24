numbers = []
def numbers_set(n):
	for i in range(n):
		print "At the top i is %d" %i 
		numbers.append(i)

		i += 1  #it doesnt matter what u do to i 
				# the next iterator doenst have effect
		print "numbers now:", numbers
		print "At the bottom i is %d" %i

numbers_set(7)
print "the numbers:"
for num in numbers:
	print num,


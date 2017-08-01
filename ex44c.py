class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD before PARENT altered"
		super(Child,self).altered()
		# call super with arguments child and self
		print "CHILD after PARENT altered"


dad = Parent()
son = Child()


# altered prints PARENT altered()
dad.altered()

# altered prints "CHILD before and after PARENT ALTERED"
son.altered()
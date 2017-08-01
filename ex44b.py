class Parent(object):

	def override(self):
		print "PARENT override()"

class Child(Parent):

	def override(self):
		print "CHILD override()"


dad = Parent()
son = Child()

# since dad belongs to class Parent it will look for override from its class first
# prints parent
dad.override()
# son is of class child it checks for override in its class before checking its super class
# prints child
son.override()
# composite basically means using another class to defind your base class
# without using any inheritance

class Other(object):
	def implicit(self):
		print "Other implicit()"

	def override(self):
		print "Other override()"

	def altered(self):
		print "Other altered()"

# not using inheritance
# madeall implicit override and altered work the sameway
# basically initiated the other class from here.
class Child(object):

	def __init__(self):
		self.other = Other() 
		# using the Other class here

	def implicit(self):
		self.other.implicit()
		# using implicit method of other
	def override(self):
		print "Child override()"

	def altered(self):
		print "CHILD before OTHER altered()"
		self.other.altered()
		print "CHILD after OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()
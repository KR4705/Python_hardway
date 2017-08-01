class Parent(object):
	def implicit(self):
		print self,"PARENT implicit()"
class Child(Parent):
	pass


dad = Parent()
son = Child()
# the method implicit is defined in parent
dad.implicit()
# the method although not defined in child it is defined in parent
# it calls the method from the parent
son.implicit()

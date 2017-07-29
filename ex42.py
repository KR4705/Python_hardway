# Class Animal is-a Object
class Animal(object):
	pass

# Class Dog is-a Animal has init with self and name as parameters
class Dog(Animal):
	def __init__(self,name):
		self.name = name
# Class Cat is-a Animal has init with self and name as parameters
class Cat(Animal):
	def __init__(self,name):
		self.name = name

# Class person which takes object
# has init method with takes self and name as parameters
class Person(object):
	def __init__(self,name):
		self.name = name
		self.pet = None

# class Employee is-a Person
# has method init which takes self,name and salary as parameters
# it calls the init method of super class of Employee and this instance
# with name as parameter
class Employee(Person):
	def __init__(self,name,salary):
		super(Employee,self).__init__(name) 
		self.salary = salary
# class Fish is an object
class Fish(object):
	pass

# class Salmon which is-a Fish
class Salmon(Fish):
	def __init__(self):
		self.type = "salmon"

	

# class Hablibut which is-a Fish
class Halibut(Fish):
	pass


# rover is-a dog
rover = Dog('rover')

# satan is-a cat
satan = Cat('satan')

# mary is-a person
mary = Person('Mary')

# Mary has a satan as pet
mary.pet = satan

# Frank is an employee
frank = Employee('Frank',120000)

# Frank has rover as pet
frank.pet = rover

# Flipper is-a first
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()

# Python always requires (object) when you make a class.

print crouse.__dict__
print dir(crouse)
# setting cars equal to 100
cars = 100
# the space in cars = 4.0 changed to 4 to make the number of people to int.
space_in_a_car = 4
# the number of driver is set to 30
drivers = 30
# total number of passengers is set to 90
passengers = 90
# the number of cars_not_driven is set to:cars - drivers 
cars_not_driven = cars - drivers
# the number of cars_driven is set to the number od drivers:drivers
cars_driven = drivers
# the carpool_capacity is set to cars_driven*space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#the average passengers_per_car os set to passengers/cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# study drill 
# you used a variable which is not defined in defining another variable.

print "Hey %s there." % "   "
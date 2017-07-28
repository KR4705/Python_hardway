# creating mapiing of state and abbrevation
# the syntax given in the textbook is giving syntax errors
# changes the square brackets to curly solved it

states = {
	'Oregan'  : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

# create basic set of states and some cities in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville',
}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' *10
print "NY state has:", cities['NY']
print "OR state has:", cities['OR']

# print some states
print "-" *10 
print "Michigan's abbrevation is",states['Michigan']
print "Florida's abbrevation is",states['Florida']

# doing it by using states then cities dict
print "-"*10
print "Michigan has: ",cities[states['Michigan']]
print "Florida has: ",cities[states['Florida']]

# print every state abbrevation
print "-"*10
# states.item() gives ??
for state,abbrevation in states.items():
	print "%s is abbrevated %s" % (state,abbrevation)

# print every city in state
print '-' *10
for abrev,city in cities.items():
	print "%s has %s city." % (abrev,city)

# now do both at the same time
print '-'*10
for state,abrev in states.items():
	print "%s has %s abbrevation and has city %s" %( 
	    state,abrev,cities[abrev])

# safely get an abbreavation by state that may not be there
print '-' * 10
state = states.get('Texas')

if not state:
	print "Sorry,no Texas"
# get a city with default value
city = cities.get('TX',"does not exist")
print city
print "The city for the state 'TX' is %s" % city




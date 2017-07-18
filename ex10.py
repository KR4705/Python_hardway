tabby_cat = "\tI'm tabbed in." #to add tabbing
persian_cat = "I'm split\non a line." #using /n to get a linebreak
backslash_cat = "I'm \\ a \\ cat " # to use backslash \\


# using triple quote you can put quotes with no need of an escape character \
fat_cat = """
I'll do a list:
\t* "Cat food" 
\t* '''Fishies''' 
\t* Catnip\n\t* Grass
"""
# prints each string variables
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,

		# the "\r" is resetting the seek to the same linkes start
		# and the output override on itself
		# the previous print. 
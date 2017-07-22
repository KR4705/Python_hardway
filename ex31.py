print "you entered a dark room with 2 doors.which room would u choose door 1 or 2"

door = raw_input("> ")

if door == "1":
	print "There is a giant bear here eating a cheese cake what would you do?"
	print "1.Take the cake"
	print "2.scream at the bear"

	bear = raw_input("> ")

	if bear == 1:
		print "The bear eats your face off! Good job!"
	elif bear ==2:
		print "the bear eats your legs away! Good job!"
	else:
		print "doing %s is probably better, bear runs away!" % bear

elif door == "2":
	print "you stare into the endless abyss at Cthulu's retina"
	print "1.Blueberries"
	print "2.Yellow jacket Clothespins"
	print "3.understanding revolvers yelling melodies"

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "your body survivies powered by the mind of jello, Congrats!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "you stumble around and fall on a knife and die. Good job!"


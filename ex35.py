from sys import exit

def gold_room():
	print "this room is full of gold.How much do you take?"

	next = raw_input('> ')
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("man,learn to type a number")

	if how_much < 50:
		print "Good you are not greedy you win"
	else:

		dead("You greedy bastard")

def bear_room():
	print "there is bear here"
	print "the bear has a bunch of honey"
	print "the fat bear is in front of another door"
	print "how are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input('> ')
		if next == "take honey":
			print "The bear looks at you and slaps your face off"
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.you can go through it now"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("the bear gets pissed, eats your legs off")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"

def cthulhu_room():
	print "Here you see the great evil cthulhu"
	print "He, it whatever stares at you,and you go insane"
	print "Do you flee for your life or eat your head"

	next = raw_input('> ')

	if 'flee' in next:
		start()
	elif 'head' in next:
		dead("well that was tasty")
	else :
		cthulhu_room()

def dead(why):
	print why , "Good job"
	exit(0)

def start():
	print "you are in a dark room"
	print "there is a door to your right and left"
	print "which one would u take?"

	next = raw_input('> ')

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("you stumble around till you starve and die")

start()	



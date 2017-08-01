from sys import exit
from random import randint


class Scene(object):

	def enter(self):
		print "Not yet configured."
		exit(1)

class Engine(object):

	def __init__(self,scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print '\n------------------'
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

	def __init__(self,n):
		self.n = n

	trolls = ['You lost connection to matrix and died.',
			  'You did not fulfil your destiny.you failed.']
	def enter(self):
		print Death.trolls[self.n]
		exit(1)

class Start_scene(Scene):

	def enter(self):
		print "Your name is neo."
		print "You work as a programmer for a coorporation at day"
		print "and work as a freelance hacker at night"
		print "you are very secretive about your operation"
		input = raw_input()
		return 'computer_scene'

class Computer_scene(Scene):

	def enter(self):
		print "One night you see your computer screen go blank"
		print "As you look at it, it displays message"
		print "'wake up, neo'"
		print "'The matrix has you.....'"
		print "You try to end the program but fail."
		print "'follow the white rabbit'"
		print "is on the screen now"
		print "'knock,knock,neo'"
		print "and you also hear your door knocked."
		print "you are scared."
		print "your customer of the night are here."
		print "They want the data you promised them."
		print "You see that the women there has a white rabbit tattoo."
		print "What do you do?"
		temp = raw_input('> ')
		if temp == 'follow':
			return 'trinity_pub'
		else:
			return 'boring_life'

class Boring_life(Scene):

	def enter(self):
		print "you wake up on your bed thinking all this is dream."
		print "You live the usual life as a hacker."
		print "You get killed by thug, whom you hacked before."
		return 'death1'

class Trinity_pub(Scene):

	def enter(self):
		print "you follow them to a pub."
		print "you do like to indulge in this kind of culture"
		print "But you wait and a women approaches you."
		print "she tells you that her name is Trinity"
		print "You know her from her hacks."
		print "she tells you in your ear that she came to warn you"
		print "that they are watching you."
		print "Next thing you remember you wake up in your bed"
		return 'office_scene'

class Office_scene(Scene):

	def enter(self):
		print "you go to office."
		print "you sit in your cabin and you get a call."
		print "You answer it 'They are here' he said."
		print "You ask who? 'They are looking for u, duck'"
		print "you duck and they start giving instructions."
		print "you follow them and reach a window unnoticed."
		print "'Jump' he said."
		print "They people you were running from see you."
		print "what will you do ?"
		action = raw_input('> ')
		if action == 'jump':
			print 'trinity catches you and takes you for ride.'
			return 'pill_scene'
		else:
			return 'bug_install'

class Bug_install(Scene):

	def enter(self):
		print "the men in suit catch you."
		print "they interogate you You told them 'I know nothing'"
		print "they open your shirt and a small bug like robot is put on ur stomach."
		print "as you scream hard, it enters your bellybutton."
		print "you wake up and feel this was a dream."
		print "you get a call and this mysterious man tells you"
		print "If you want answers go to the adams bridge."
		print "You go and find yourself picked up by a car."
		print "there is trinity with you and a woman with gun pointed at you."
		print "They remove the bug using some device from your belly."
		print "You realize it was not a dream."
		return 'pill_scene'

class Matrix_room(Scene):

	def enter(self):
		print "Congratulations, You train hard and become"
		print "the ONE."
		print "----------------------------"
		print "             the end"
		exit(0)
class Pill_scene(Scene):

	def enter(Self):
		print "you are then made to meet morphius."
		print "you ask him about matrix."
		print "no one can see what the matrix is you have to see it by yourself, he said"
		print "he then opens a small box having two pills"
		print "Take blue pill and your life goes back to way it was,you wake up in your bed"
		print "and believe what you want to beleive"
		print "take the red pill and ill show you how deep the rabbit hole goes."

		pill = raw_input('> ')
		if pill == 'blue':
			return 'boring_life'
		elif pill == 'red':
			return 'matrix_room'
		else:
			print "you take too long and they leave.men in suit come and attack you."
			return 'death1'
			


class Map(object):

	scenes = {
		'start_scene' : Start_scene(),
		'matrix_room' : Matrix_room(),
		'bug_install' : Bug_install(),
		'office_scene' : Office_scene(),
		'trinity_pub' : Trinity_pub(),
		'computer_scene' : Computer_scene(),
		'boring_life' : Boring_life(),
		'pill_scene' : Pill_scene(),
		'death0' : Death(0),
		'death1' : Death(1)
 	}

 	def __init__(self):
		self.start_scene = 'start_scene'

	def next_scene(self,scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map()
a_game = Engine(a_map)
a_game.play()


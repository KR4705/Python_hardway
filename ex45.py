from helper import print_board
from helper import swap

array = []
# size of array
size = 4
# init end_game array
end_game = []
bot_e = [1,2,3,4]
mid_e = [5,6,7,8]
top_e = [9,10,11,12]
top_e2 = [13,14,15,0]
end_game.append(bot_e)
end_game.append(mid_e)
end_game.append(top_e)
end_game.append(top_e2)
# setting up board
bot = [1,2,3,4]
mid = [5,6,7,8]
top = [9,10,11,12]
top_1 = [13,14,0,15]
array.append(bot)
array.append(mid)
array.append(top)
array.append(top_1)

# printing the board
print "The board is:"
print_board(array)
# printing goal array
print "This is the board you need to make"
print_board(end_game)

active = True
while active:
	# printing possible choices
	for each in array:
		if 0 in each:
			i = array.index(each)
			j = each.index(0)
	zero_pos = i,j
	poss_ij =[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
	for each in poss_ij:
		if not each[0] in range(size) or not each[1] in range(size):
			poss_ij.remove(each)
	#making array of possible choices
	poss_num = [] 
	for each in poss_ij:
		poss_num.append(array[each[0]][each[1]])
	print "possible moves are on numbers :"
	for each in poss_num:
		print each , 
	print ""
	choice = '$$$$'
	while not choice in poss_num:
		choice = raw_input('> ')
		choice = int(choice)
	print "making move for choice %r" % choice
	array = swap(choice,array)
	# printing the board
	print "after your move"
	print_board(array)
	active = not array == end_game
	if not active:
		print "Congrats bro!!"

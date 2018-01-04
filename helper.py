
def print_board(array):
	for each in array:
		print each

def swap(num,array):
	zero_index,num_index = (-1,-1),(-1,-1) 
	# finding index of num in array
	for each in array:
		if 0 in each:
			zero_index = array.index(each),each.index(0)
		if num in each:
			num_index = array.index(each),each.index(num)
	array[zero_index[0]][zero_index[1]] = num
	array[num_index[0]][num_index[1]] = 0
	return array



from sys import argv

script , file_name = argv

#prints all the data in the file

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0) 
     # set seek to 0 means to the start 
     # count of bytes before the seek

def print_a_line(line_count,f):
	print line_count,f.readline()
	# readline() gives the out put of the remaining line from seek.

current_file = open(file_name)

print "First lets print the whole file"
print_all(current_file)

print current_file.tell() # tell tells us where the seek is
# read puts the seek at the end of file.
 
# without seek being set to 0 the output of the
# code below would be nil
print "Now lets rewind"
rewind(current_file)

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
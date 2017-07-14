from sys import argv

script,  filename = argv

print "We are going to erase file:%r" % filename
print "If you dont want it hit CTRL+C(^C)."
print "If you want this hit RETURN(enter)."

raw_input("?") # this does not do anything except the fact that 
# it is stopping script from running till you give an input.

print "Opening the file ..."
target = open(filename, 'w') # we gave argument of 'w' to the file 
# this makes the file writable but the file is not readable.
# print target.read()  ::: and error saying file not open for read.
print "truncating the file.Goodbye!"
target.truncate()

print "now I am going to ask you for three lines"

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I am gonna write these lines to the file"
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# because we had to give line break, means that write just writes right after the end of file data.

print "And finally we close it."
target.close()




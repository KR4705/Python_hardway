# ex14.py
from sys import argv

script,user_name= argv #unpacking the arguments to script and user_name
prompt = '> ' #changing the value of prompt here would 
# change the prompt for all raw_input

# this is taking the args
print "Hi %s i am the %s script" %(user_name,script) 
print "I would like to ask you a few questions"
print "Do you like me %s?"%user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of a computer do you have?"
computer = raw_input(prompt)

print """
alright you said about %r about liking me.
you live in %r . not sure where this is.
you said you have %r kind of computer. Nice.
""" % (likes, lives, computer)
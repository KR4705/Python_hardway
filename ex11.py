# ex11.py
# print "How old are you?" ,
age = input("How old are you?") #can give phrase to the function
# and its prints for us. raw_input() always gives us the uninterpretted output as string.
print "how tall are you?" ,
height = raw_input()
print "How much do you wight?" ,
weight = raw_input()

# input() gives us the interpreted type of the input

print "so you are %r years old, %r tall and %r heavy." %(age,height,weight)

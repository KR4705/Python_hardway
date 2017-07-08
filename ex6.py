# %d is for numbers digits variables as seen before its also only for int type
x = "there are %s type of people." % "10"
binary = "binary"
do_not = "don't"
# %s is for string type variable to be put in string
y = "those who know %s are those who %s" % (binary,do_not)

print x
print y
# didnt get much difference in %r and %s except that %r gives quotes around the variable.
print "i said %r" % x
print "i also said %s" % y

hilarious = False
# we can break the %r or %s or %d and put the variable in the string when printing too.
joke_evaluation = "Isnt that joke so funny? %r"

print joke_evaluation % hilarious

w = "this is left side of..."
v = "this is right side of..."

print w + v

# %r is used for debugging as it displays raw data

#drill
# string is put inside string at lines : 2, 6, 6,12
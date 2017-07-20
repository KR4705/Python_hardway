print "Let's practice everything!!"
print "You\'d need to know \'bout escapes with // that do /n newlines and /t tabs"

poem = """
\t the lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere this is none.
"""

print "----------------"
print poem
print "----------------"


five = 10 - 2 + 3 -6
print "this should be five: %s" % five  # auto type casted

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates #this returns a tuple respectively

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print "with the starting point of %s" %start_point #normal usage of string function.
print "we would have %d beans,%d jars and %d crates."% (beans,jars,crates)

start_point = start_point/10

print "we also can do that this way"  #giving the string function a tuple as input.
print "we would have %d beans,%d jars and %d crates."% secret_formula(start_point)

  



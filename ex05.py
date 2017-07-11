my_name = "Rohith Sreeramdas"
my_age = 26 
my_height = 71 #inches
my_weight = 142.7 #kilos
my_weight_pounds = my_weight * 2.20462 #pounds
my_height_cm = my_height * 2.54 #centi meters

print "let's talk about %s" % my_name
print "he's %s years old" % my_age
print "his height is %s and his weight is %s" % (my_height_cm,round(my_weight_pounds))
# %d for int type even though i gave weight as float it had
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)


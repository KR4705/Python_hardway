# just setting the string given into var days
days = "sun mon tue wed thu fri sat"
# the \n is the symbol for linebreak. setting string to var months
months = "Jan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug\nSep\nOct\nNov\nDec"
# prints first then the next which is days
print "here are the days :" , days
print "here are the months : \n" , months
# multi line printing the triple double-quote is the syntax for that.
print """
There's something going on here.
With the three double-quotes,
we can type as much as we like.
Even 4 lines or 5 or 6.
"""
# the %r take the raw data and wont consider the value in it to take line break.
test = "... %r  working" % "\n" 
print test
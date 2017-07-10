formatter = "%r %r %r %r" # %r is for raw data but the values of %r are not given.
#note the formatter is string object
# print formatter
print formatter %(1,2,3,4) 
#we gave 1,2,3,4 as the 4 %r values to formatter and print.
print formatter %("one","two","three","four") 
# gave String one two three four to formatter.
print formatter %(True , False , False , True)
#gave boolean values true false false true 
print formatter %(formatter, formatter, formatter, formatter)
# no idea what this does.. gave output as '%r %r %r %r' * 4
print formatter % (
	"I had this thing." ,
	"That you could type upright." ,
	"But it didn't sing." ,
	"So I said goodnight."
)# gave the strings in each line as input to %r of formatter 
# sets the variable 'formatter' as a string literal with four undefined raw references
formatter = "%r %r %r %r"

# prints the variable 'formatter' using as references four integers
print formatter % (1, 2, 3, 4)
# prints the variable 'formatter' using as references four string literals
print formatter % ("one", "two", "three", "four")
# prints the variable 'formatter' using as references four boolean values
print formatter % (True, False, False, True)
# prints the variable 'formatter' using as references the string contained in the variable 'formatter'
print formatter % (formatter, formatter, formatter, formatter)
# prints the variable 'formatter' using as references four string literals
# the last line of output uses double quotes because a single quote is used inside the string
# literal, and it's meant for preventing ambiguity
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)


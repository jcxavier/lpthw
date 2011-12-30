# sets the value of the variable 'x' as a string literal with a reference to an integer literal
x = "There are %d types of people." % 10
# sets the value of the variable 'binary' as a string literal
binary = "binary"
# sets the value of the variable 'do_not' as a string literal
do_not = "don't"
# sets the value of the variable 'y' as a string literal with references to two variables
# containing strings (2 strings inside a string)
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the content of the variable 'x'
print x
# prints the content of the variable 'y'
print y

# prints the string literal with a raw reference to the variable 'x' (3 strings inside a string)
print "I said: %r." % x
# prints the string literal with a reference to the variable 'y' as a string
print "I also said: '%s'." % y

# sets the value of the variable 'hilarious' as the boolean value of False
hilarious = False
# sets the value of the variable 'joke_evaluation' as a string literal with a raw and undefined
# reference
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the variable 'joke_evaluation' using the variable 'hilarious' as a raw reference (4 strings
# inside a string)
print joke_evaluation % hilarious

# sets the value of the variable 'w' as a string literal
w = "This is the left side of..."
# sets the value of the variable 'e' as a string literal
e = "a string with a right side."

# prints the string contained in the variable 'w' concatenated with the string contained
# in the variable 'e'
print w + e


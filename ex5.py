name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
# convert inches to cms
height_cm = height * 2.54
# convert lbs to kgs
weight_kg = weight * 0.45359237

# %0.2f formats the floating point number to show only two decimal places
print "%d inches is %0.2f centimeters" % (height, height_cm)
print "%d pounds is %0.2f kilograms" % (weight, weight_kg)
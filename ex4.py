# declare 'cars' is equal to 100
cars = 100
# declare 'space_in_a_car' is equal to 4.0 (for supporting floating point operations)
space_in_a_car = 4.0
# declare 'drivers' is equal to 30
drivers = 30
# declare 'passengers' is equal to 90
passengers = 90
# declare 'cars_not_driven' is the subtraction of the variable 'drivers' from the variable 'cars'
cars_not_driven = cars - drivers
# declare 'cars_driven' is equal to the variable 'drivers'
cars_driven = drivers
# declare 'carpool_capacity' is equal to the floating point product of the variable 'cars_driven'
# and the variable 'space_in_a_car'
carpool_capacity = cars_driven * space_in_a_car
# declare 'average_passengers_per_car' is equal to the integer division of the variable 'passengers'
# by the variable 'cars_driven'
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
#
# This is due either to a typo in the variable definition of 'car_pool_capacity' or a lack of definition
# for this variable.
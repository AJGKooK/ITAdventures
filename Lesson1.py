# Created by Aaron Goff

# Allow user to nput two numbers
number1 = int(input("First number: "))
number2 = int(input("Second number: "))

# Add/Subtract/Multiply/Divide the numbers, convert operations to strings once completed, and assign them to new string variables
addition = str(number1 + number2)
subtraction = str(number1 - number2)
multiplication = str(number1 * number2)
division = str(number1 / number2)

# Print out the two input numbers and the modified operation
print('addition of of %s and %s is %s' % (number1, number2, addition))
print('subtraction of %s and %s is %s' % (number1, number2, subtraction))
print('multiplication of %s and %s is %s' % (number1, number2, multiplication))
print('division of %s and %s is %s' % (number1, number2, division))
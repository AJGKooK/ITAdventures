# Created by Aaron Goff

# Allow user to nput two numbers & operator
number1 = int(input("The first number, please: "))
Operator = input("Enter in an operator: ")
number2 = int(input("The second number, if you would be so kind: "))

# Use if, elif, and else to determine which single operation to perform
# Surround if, elif, and else statements with try/except to catch a 'divide by zero' fault
try:
    if Operator == '+':
        print(number1 + number2)
    elif Operator == '-':
        print(number1 - number2)
    elif Operator == '*':
        print(number1 * number2)
    elif Operator == '/':
        print(number1 / number2)
    else:
        # If operator input is not found, inform user
        print("You did not give a recognized operator")
except ZeroDivisionError:
    print("You can't divide by zero!")
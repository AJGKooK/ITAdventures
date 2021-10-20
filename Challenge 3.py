# Created by Aaron Goff
# YouTube Walk-Through: https://www.youtube.com/watch?v=JS9YoIOZTWE&list=PLBawh3P7dWoURbtf93DZwxW70LuZEBoGz&index=10

# Create a while True loop (infinite loop)
while True:
    # Create operator and input numbers to prime future while loops
    operator = None
    number1 = None
    number2 = None

    # Run loop until a known operator is entered, or end is called
    while operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "end":
        operator = input("Enter in an operator: ")

    # If the operator is "end", then number inputs are not required
    if operator != "end":
        # Loop until the user inputs an int, if an int is not input, prompt user again
        while type(number1) != int:
            try:
                number1 = int(input("Number 1: "))
            except ValueError:
                continue

        # Loop until the user inputs an int, if an int is not input, prompt user again
        while type(number2) != int:
            try:
                number2 = int(input("Number 2: "))
            except ValueError:
                continue

    # Use if, elif, and else to determine which single operation to perform
    # Surround if, elif, and else statements with try/except to catch a 'divide by zero' fault
    try:
        if operator == '+':
            print("%s + %s = %s" % (number1, number2, number1 + number2))
        elif operator == '-':
            print("%s - %s = %s" % (number1, number2, number1 - number2))
        elif operator == '*':
            print("%s * %s = %s" % (number1, number2, number1 * number2))
        elif operator == '/':
            print("%s / %s = %s" % (number1, number2, number1 / number2))
        else:
            # Break from the original main loop and end the program when "end" is entered for operator
            if operator == "end":
                print("Goodbye!")
                break
    except ZeroDivisionError:
        print("You can't divide by zero!")

# Basic Calculator
# For CIT 95 Giraffe Academy Assignment
# Inspired by Giraffe Academy "Basic Calculator" example
# by Mark Edmunds
# August 18, 2023.
# User Input Validation

# make sure the user inputs a valid number
def validate_input(userinput) -> float:
    """

    :type userinput: str
    """
    try:
        number = float(userinput)
        return number
    except ValueError:
        return validate_input(input("Not a number try again: "))


# makes sure user input a valid operation
def validate_operation(userinput) -> str:
    if operation_set.__contains__(userinput):
        return userinput
    else:
        return validate_operation(input("Enter a valid arithmetic operation: "))


# performs calculation
def calculate(safe_num1, safe_num2, operation) -> float:
    """

    :type operation: str
    :type safe_num1: float
    :type safe_num2: float
    """

    def addition():
        return safe_num1 + safe_num2

    def subtraction():
        return safe_num1 - safe_num2

    def multiple():
        return safe_num1 * safe_num2

    def divide():
        return safe_num1 / safe_num2

    if operation == "+":
        return addition()
    elif operation == "-":
        return subtraction()
    elif operation == "*":
        return multiple()
    else:
        return divide()


# literals
num1 = (validate_input(input("Enter number: ")))
num2 = (validate_input(input("Enter second number: ")))
operation_set = {"+", "-", "*", "/"}
operator = validate_operation(input("Enter the operation you want to perform: "))
total = calculate(num1, num2, operator)

# output
print(total)

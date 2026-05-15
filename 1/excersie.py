# Build a Python Calculator that can perform basic arithmetic operations (addition, subtraction, multiplication, division) and also include functions for exponentiation and modulus.
# The calculator should be able to handle user input and provide results based on the selected operation.

a = float(input("Enter the first number: "))  # Taking user input for the first number and converting it to a float
b = float(input("Enter the second number: "))  # Taking user input for the second number and converting it to a float

operation = input("Enter the operation (+, -, *, /, **, %): ")  # Taking user input for the desired operation
if operation == '+':  # Checking if the operation is addition
    result = a + b  # Performing addition
elif operation == '-':  # Checking if the operation is subtraction
    result = a - b  # Performing subtraction    
elif operation == '*':  # Checking if the operation is multiplication
    result = a * b  # Performing multiplication
elif operation == '/':  # Checking if the operation is division
    if b != 0:  # Checking if the second number is not zero to avoid division by zero error
        result = a / b  # Performing division
    else:
        result = "Error: Division by zero is not allowed."  # Handling division by zero case
elif operation == '**':  # Checking if the operation is exponentiation
    result = a ** b  # Performing exponentiation
elif operation == '%':  # Checking if the operation is modulus
    if b != 0:  # Checking if the second number is not zero to avoid modulus by zero error
        result = a % b  # Performing modulus operation
    else:
        result = "Error: Modulus by zero is not allowed."  # Handling modulus by zero case
else:
    result = "Error: Invalid operation."  # Handling invalid operation case

print(f"The result of {a} {operation} {b} is: {result}")  # Displaying the result of the calculation
# conditional expression is one-line shortcut for if-else statements (ternary operator)
# Print or assign a value based on a condition in a single line of code
# x if condition else y
while True:
    num = int(input("Enter a number: "))
    result = "Even" if num % 2 == 0 else "Odd"
    print(f"The number {num} is {result}.")

    print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    max_num = a if a > b else b
    print(f"The maximum number is: {max_num}")
    min_num = a if a < b else b
    print(f"The minimum number is: {min_num}")

    age = int(input("Enter your age: "))
    status = "Adult" if age >= 18 else "Minor"
    print(f"You are an {status}.")
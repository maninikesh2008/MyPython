# Type casting in Python is the process of converting a variable from one data type to another. 
# There are two main types of Python type conversion:

# Implicit Type Conversion: Performed by the Python interpreter automatically.

# Explicit Type Conversion: Performed by a Python programmer manually.

# 1. Implicit Type Conversion in Python
# In Python Type Conversion, implicit conversion happens automatically when we mix different data types in an expression. Python safely converts 
# one type to another without losing data.

# For example, if we add an integer to a float, Python converts the integer to a float before performing the operation.

x = 5  # int
y = 3.2  # float
result = x + y  # Implicitly converts x to float
print(f"Implicit Conversion: {result}")  # Output: 8.2
# In this example, the integer 5 is implicitly converted to a float before the addition operation, resulting in a float output.


# 2. Explicit Type Conversion in Python
# Explicit Type Conversion in Python is when we manually change the data type of a value using built-in functions like int(), float(), str(), etc. It gives us more control over data types.
# This process is also called type casting in Python. We use it when Python doesn’t automatically convert data types, especially when combining different types like strings and numbers.

# Example of explicit type conversion

num_str = "50"        # string
num_int = int(num_str)  # converting string to integer
result = num_int + 10
result_str = str(result)  # converting the result back to string
num_bool = bool(num_int)
num_int2 = 0
num_bool2 = bool(num_int2)
print("Result:", result)
print("Type of result:", num_str, type(num_str))  # Checking the type of num_int after conversion
print("Type of result:", num_int, type(num_int))  # Checking the type of num_int after conversion
print("Type of result:", result, type(result)) # built-in function type() to check the data type of the result
print("Type of result:", result_str, type(result_str)) # Checking the type of result_str after conversion
print("Type of result:", num_bool, type(num_bool)) # Checking the type of num_bool after conversion
print("Type of result:", num_bool2, type(num_bool2)) # Checking the type of num_bool2 after conversion
# In this example, we explicitly convert the string "50" to an integer using the int
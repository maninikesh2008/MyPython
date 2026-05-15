# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# Types: String, int, float, bool

first_name = "John"  # String
age = 30  # int
height = 5.9  # float
height2 = "5.9"  # string
is_student = True  # bool
# Multiple assignment
x, y, z = 1, 2.5, "Hello"  # int, float, string 
# Output variables
print(first_name)
print(age)
print(height)
print(height2)
print(is_student)
print(x, "\n", y, z)
print(y)
print(z)        
print(f"First Name: {first_name}, Age: {age}, Height: {height}, Is Student: {is_student}")  # Multiple variables in one print statement


if is_student:
    print(f"{first_name} is a student.")
else:    print(f"{first_name} is not a student.")

if if_online := False:  # Using the walrus operator to assign and check the variable in one line
    print(f"{first_name} is Online.")
else:    print(f"{first_name} is not Online.")
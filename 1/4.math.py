# Python provides mathematical capabilities through built-in functions (available without importing), the math module (standard library for real numbers), 
# and specialized modules like cmath
import math  # Importing the math module to access additional mathematical functions
num1 = print(math.pi)
print(num1) 
num1 = math.sqrt(16)  # Using the math.sqrt() function to calculate the square root of 16
print(num1)
num1=round(num1)  # Using the built-in round() function to round num1 to the nearest integer
print(num1) 
num1 = num1 + 5  # Using the addition operator to add 5 to num1
num1 += 5  # Using the augmented assignment operator to add 5 to num1 or num1 = num1 + 5 
print(num1) 
num1 -= 2  # Using the augmented assignment operator to subtract 2 from num1 or num1 = num1 - 2
print(num1) 
num1 *= 3  # Using the augmented assignment operator to multiply num1 by 3 or num1 = num1 * 3
print(num1) 
num1 /= 4  # Using the augmented assignment operator to divide num1 by 4 or num1 = num1 / 4
print(num1)
num1 **= 2  # Using the augmented assignment operator to raise num1 to the power of 2 or num1 = num1 ** 2
print(num1)
remainder = num1 % 3  # Using the modulus operator to find the remainder of num1 divided by 3
print(remainder)
num1 //= 2  # Using the augmented assignment operator to perform floor division on num1 by 2 or num1 = num1 // 2



if num1 > 0:
    print(f"{num1} is positive.")
elif num1 < 0:
    print(f"{num1} is negative.")
else:    print(f"{num1} is zero.")

num1 = abs(num1)  # Using the built-in abs() function to get the absolute value of num1 or 

print(num1)  # Output: 10

radius = num1  # Assigning num1 to radius for calculating the area of a circle
area_of_circle = math.pi * radius ** 2  # Using the formula for the area of a circle (A = πr^2) to calculate the area based on the radius   
print(f"The area of the circle with radius {radius} is: {area_of_circle}")  # Displaying the calculated area of the circle
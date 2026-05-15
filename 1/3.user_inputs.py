# In Python, the input() function is the primary way to collect data from a user. When called, 
# it pauses the program and waits for the user to type something and press the "Enter" key.

input_string = input("Please enter a string: ")  # Collecting a string input from the user
input_number = input("Please enter a number: ")  # Collecting a number input from
name = input("What is your name? ")  # Collecting the user's name
age = input("How old are you? ")  # Collecting the user's age
#age = age +1  # This will cause an error because age is a string and we cannot add an integer to it. We need to convert age to an integer first.
age = int(age)  # Converting the age input from string to integer
age = age + 1  # Now we can add 1 to the age variable without causing an error.


print(f"Hello, {name}! You are {age} years old.")  # Using f-string to display the collected information
print(f"You entered the string: {input_string}")  # Displaying the string input
print(f"You entered the number: {input_number}")  # Displaying the number input 

# Mad Libs Game
print("\nLet's play a Mad Libs game!")
noun = str(input("Enter a noun: "))
verb = str(input("Enter a verb: "))
adjective = str(input("Enter an adjective: "))
adverb = str(input("Enter an adverb: "))
mad_libs_result = f"The {adjective} {noun} {verb} {adverb}."
print(mad_libs_result)  # Displaying the result of the Mad Libs game
# example of Madlab game where the user is prompted to enter a noun, verb, adjective, and adverb, and then the program constructs a sentence using those inputs.
# Example input: noun = "Lion", verb = "jumps", adjective = "lazy", adverb = "quickly"

# Calculate Area of a rectangle
print("\nLet's calculate the area of a rectangle!")
length = float(input("Enter the length of the rectangle: "))  # Collecting the length input and converting it to float
width = float(input("Enter the width of the rectangle: "))  # Collecting the width input and converting it to float

area = length * width  # Calculating the area of the rectangle
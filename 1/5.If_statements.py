# In Python, an if statement is used to execute a block of code only if a specific condition is met. 
# It is the most fundamental tool for decision-making and controlling the flow of a program
# if .. do something elif .. do something else else .. do something else
import datetime  # Importing the datetime module to work with dates and times
current_year = datetime.datetime.now().year  # Getting the current year using the datetime module

age = int(input("Enter your age: "))  # Taking user input for age and converting it to an integer
if age >= 18:  # Checking if the age is greater than or equal to
    print("You are an adult.")  # If the condition is true, this line will be executed
elif age >= 13:  # If the previous condition is false, this condition will be
    print("You are a teenager.")  # If the condition is true, this line will be executed
else:  # If all previous conditions are false, this block will be executed
    print("You are a child.")  # This line will be executed if the age is less than 13

birth_year = int(input("Enter your birth year: ")) 
# Taking user input to check if you are boomer or genz or genalpha  
if birth_year < 1946:
    print("You are from the Silent Generation.")
elif 1946 <= birth_year < 1965:
    print("You are a Baby Boomer.")
elif 1965 <= birth_year < 1981:
    print("You are from Generation X.")
elif 1981 <= birth_year < 1997:
    print("You are a Millennial.")
elif 1997 <= birth_year < 2013:
    print("You are from Generation Z.")
else:
    print("You are from Generation Alpha.")
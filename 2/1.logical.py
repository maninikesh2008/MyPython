# Logical Operator used to combine two or more conditions. The result is true if at least one of the conditions is true.(check if at least one condition is true)

# AND(and) = check two or more conditions and return true if all conditions are true
# OR(or) = check two or more conditions and return true if at least one condition is true
# NOT(not) = check a condition and return true if the condition is false

temp = int(input("Enter the temperature: "))

if temp > 16 and temp < 30:
    print("The weather is nice")
elif temp >= 30 or temp <= 36:
    print("The weather is hot")
elif not temp < 16:
    print("The weather is cold")
else:
    print("The weather is not nice")

choice = input("Enter 1 to convert Centigrade to Fahrenheit, or 2 to convert Fahrenheit to Centegrade")
if choice == '1':
    cent = float(input("Enter temp in Centegrade: "))
    fahr = (cent* 9/5) + 32
    print(f"{cent} degrees Centigrade is equal to {fahr} degrees Fahrenheit.")
elif choice == '2':
    fahr = float(input("Enter temp in Fahrenheit: "))
    cent = (fahr - 32) * 5/9
    print(f"{fahr} degrees Fahrenheit is equal to {cent} degrees Centigrade.")
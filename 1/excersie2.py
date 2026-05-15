# Python code for weight conversion from pounds to kilograms and vice versa, use a choice to select the conversion direction, and handle user input for weight values. The code includes functions for both conversions and displays the results with appropriate formatting.
def pounds_to_kilograms(pounds):
    """Convert pounds to kilograms."""
    kilograms = pounds * 0.45359237  # 1 pound is equal to 0.45359237 kilograms
    return kilograms

def kilograms_to_pounds(kilograms):
    """Convert kilograms to pounds."""
    pounds = kilograms / 0.45359237  # 1 kilogram is equal to 2.20462262185 pounds
    return pounds
# Example usage:
choice = input("Enter '1' to convert from pounds to kilograms, or '2' to convert from kilograms to pounds: ")  # Taking user input for conversion choice
if choice == '1':
    weight_in_pounds = float(input("Enter weight in pounds: "))  # Taking user input for weight in pounds and converting it to a float
    weight_in_kilograms = pounds_to_kilograms(weight_in_pounds)  # Converting the weight from pounds to kilograms
    print(f"{weight_in_pounds} pounds is equal to {weight_in_kilograms:.2f} kilograms.")  # Displaying the result with 2 decimal places
elif choice == '2':
    weight_in_kilograms = float(input("Enter weight in kilograms: "))  # Taking user input for weight in kilograms and converting it to a float
    weight_in_pounds = kilograms_to_pounds(weight_in_kilograms)  # Converting the weight from kilograms to pounds
print(f"{weight_in_kilograms} kilograms is equal to {weight_in_pounds:.2f} pounds.")  # Displaying the result with 2 decimal places
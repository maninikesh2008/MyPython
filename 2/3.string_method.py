name = str(input("Enter your name: "))

length = len(name)
print("The length of your name is:", length)

first_char = name[0]
print("The first character of your name is:", first_char)

last_char = name[-1]
print("The last character of your name is:", last_char) 

upper_name = name.upper()
print("Your name in uppercase is:", upper_name) 

lower_name = name.lower()
print("Your name in lowercase is:", lower_name)    

duplicates = len(name) != len(set(name))
print("Has Duplicate" if duplicates else "No Duplicate")

def list_duplciate(name):
    seen = set()
    duplicates_arr = set()
    for char in name:
        if char in seen:
            duplicates_arr.add(char)
        else:
            seen.add(char)
    return list(duplicates_arr)
print("Duplicate characters in your name:", list_duplciate(name))
# Concept 1: Variables
# Write a python script that defines & initializes:
# One integer variable
# One float variable
# One string variable
# Then print each variable.

integer = 5
floating_point = 3.14
string = "Hello, World!"
print(integer)
print(floating_point)
print(string)

# Concept 2: Type Casting
# Define some string variable and set it equal to "17".
# Then use the int() function to typecast it into an integer.
# Print the value before and after typecasting.

some_string_variable = "17"
print(some_string_variable)
some_integer_variable = int(some_string_variable)
print(some_integer_variable)

# Concept 3: Lists
# Create a list that contains 5 numbers.
# Print the list using the print() function.
# Print the third item in the list (stored at index 2).
# Add an item to the list using the append() function.
# Print the list again using the print() function.

numbers = [0, 5, 10, 15, 20]
print(numbers)
print(numbers[2])
numbers.append(25)
print(numbers)

# Concept 4: For Loops
# Create a list that contains 5 names.
# Loop the list using a for loop and print each name in this list.
# Add a name to the list.
# Print the length of the list.

names = ["Alice", "Bob", "Charlie", "David", "Edward"]
for name in names:
    print(name)
names.append("Frank")
print(len(names))

# Concept 5: Comments
# Add comments to any of the code in the exercises above.
# Make sure to include one commented line, and one commented block (multiple lines).

# This is a commented line.

"""
This is a
commented
block
"""

# Concept 6: Dictionaries
# Create a dictionary that holds the names and phone numbers of 3 persons.
# Use the names as keys and the phone numbers as values.
# Print the dictionary.
# Print the dictionary's keys.
# Print the dictionary's values.
# Print the dictionary's items.
# Add the phone number of "Raj" to the dictionary.
# Print the phone number of "Raj". Extract the number from the dictionary using the key "Raj".
# Print the dictionary.
# Remove Raj's phone number from the dictionary.
# Print the dictionary.
# Print the names (keys) in the dictionary using a for loop.
# Print the phone numbers (values) in the dictionary using a for loop.

dictionary = {
    "Alice": "321-456-0987",
    "Bob": "987-456-3210",
    "Charlie": "465-321-0987",
}
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
dictionary["Raj"] = "321-098-4567"
print(dictionary["Raj"])
print(dictionary)
dictionary.pop("Raj")
print(dictionary)
for key in dictionary.keys():
    print(key)
for value in dictionary.values():
    print(value)

# Concept 7: File Handling
# Download this file: names.txt
# Write a script that opens this file in the "reading" mode,
# uses a for loop to scan the file, read each line and print it.

with open("names.txt", "r") as file:
    for line in file.readlines():
        print(line.strip())

# Concept 8: Extracting Rows, Attributes from File
# Use this file: names.txt
# Write a script that extracts the ages of all people and prints them.
# Use a for loop & the split() function to split each row into (name, age).
# Use the int() function to convert the extracted age from string to integer.

with open("names.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        name, age_str = line.split()
        age = int(age_str)
        print(age)

# Concept 9: Pandas Data Frames
# Use this file: names.txt
# Write a script that reads this file into a dataframe.
# Find the max and min age.
# Using the loc indexing operator, extract rows 2 & 3.

import pandas as pd
df = pd.read_csv("names.txt", sep="\t", names=["name", "age"])
print(df["age"].max())
print(df["age"].min())
extracted_rows = df.loc[2:3]
print(extracted_rows)

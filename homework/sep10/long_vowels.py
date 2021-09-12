# 6. Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to 
# the length of 5.

long_vowels = ["aa", "ee", "ii", "oo", "uu"]

# takes input from user
message = input("Give me a message, and I'll make your double vowels looooog!: ").lower()
print("")

# creates new string for output after manipulation of input message
output_message = ""

# loop through each character in input message and append changes to output message

for char in range(len(message)):
    doubles = message[char: char + 2]
    if doubles in long_vowels:
        output_message += message[char] * 4
    else:
        output_message += message[char]
print(output_message)
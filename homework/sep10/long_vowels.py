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

for char in message:
    c = char
    index = 1
    if char == message[index + 1]:
        output_message += char * 5
    
    else:
        output_message += char
    index += 1
print(output_message)
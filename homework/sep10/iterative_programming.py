# Iterative Programming Homework 9/10/21
# # 1. Multiply Vectors
# # Given two lists of numbers of the same length, create a new list by multiplying the 
# # pairs of numbers in corresponding positions in the two lists. Example:

# # [2, 4, 5] x [2, 3, 6] = [4, 12, 30]


arr1 = [2, 4, 5]
arr2 = [2, 3, 6]
multiplied = []

index = 0

while index < len(arr1): # will loop while index is less than the length of arr1(3)
    multiplied.append(arr1[index] * arr2[index]) # appends index of arr1 * index of arr2 to "multiplied" list
    index +=1 # index increases by one before loop starts again
print(multiplied) 

print("\n ----- \n")

# 2. Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is 
# represented as an list of lists:

# [ [2, -2],
#    [5, 3] ]
# Calculate the result of adding the two matrices. The number in each position in the 
# resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add

# 1 3
# 2 4
# and

# 5 2
# 1 0
# results in

# 6 5
# 3 4


matrix1 = [ [1, 3],
            [2, 4] ]

matrix2 = [ [5, 2],
            [1, 0] ]

matrix3 = [] # inner list
sums = [] # outer list

for index1 in range(len(matrix1)):                                      # index --> [0] <- changes "row"
    matrix3 = []                                                        # creates list for list-ception (inner list)
    for index2 in range(len(matrix2)):                                  # index (points to second number in index,
                                                                        # so when this loops, will go through the following... --> [0][0], [0][1] 
                                                                        # changes "column"
                                                                        # in next loop of outer, "row" is changed, so will loop throught the following: [1][0], [1][1]
        matrix3.append(matrix1[index1][index2] + matrix2[index1][index2]) # add to matrix3: 
                                                                        # (m1[0][0] + m2[0][0]), continues to loop
    sums.append(matrix3)                                                # adds matrix3 to sums list (outer list)
    print(matrix3)                                                      # prints inside list
print(sums)                                                             # print outer list (contains inner list)

print("\n ----- \n")

# 3. Matrix Addition II
# Use your solution in Matrix Addition, and extend it to work for a pair of matrices 
# of any size, as long as they have the same size.

matrix1 = [ [1, 3, 1],
            [2, 4, 1],
            [5, 6, 1],
            [9, 10, 1]]

matrix2 = [ [5, 2, 2],
            [1, 0, 3],
            [7, 8, 4],
            [1, 2, 3]]

matrix3 = [] # inner list
sums = [] # outer list

if len(matrix1) == len(matrix2):                                            # checks that matrices are same size
    for index1 in range(len(matrix1)):                                      # index --> [0] <- changes "row"
        matrix3 = []                                                        # creates list for list-ception (inner list)
        for index2 in range(len(matrix2)-1):                                # index (points to second number in index,
                                                                            # so when this loops, will go through the following... --> [0][0], [0][1] 
                                                                            # changes "column"
            matrix3.append(matrix1[index1][index2] + matrix2[index1][index2]) # add to matrix3: 
                                                                            # (m1[0][0] + m2[0][0]), continues to loop
        sums.append(matrix3)                                                # adds matrix3 to sums list (outer list)
        print(matrix3)                                                      # prints inside list
    print(sums)                                                             # print outer list (contains inner list)
elif len(matrix1) != len(matrix2):                                          # if not same size, statement below prints
    print("Matrices are not the same size")

print("\n ----- \n")

# 4. De-dup
# Given a list of numbers or strings, create a new list containing the same elements 
# as the first list, except with any duplicate values removed. Print the list.

my_list = [1, 2, 3, 1, 1, 2, 3, 1, 3]
new_list = []

for item in my_list:                                # for each number item in my_list
    if item not in new_list:                        # checks if item is included in new_list
        new_list.append(item)                       # if not, adds number to new_list
print(new_list)

print("\n ----- \n")

# 5. Leetspeak
# Given a paragraph of text as a String, print the paragraph in leetspeak.

# To translate a String to leetspeak, you need to replace make the following character 
# replacements (treat all input characters as uppercase):

# Letter	Translates To
#   A	         4
#   E	         3
#   G	         6
#   I	         1
#   O	         0
#   S	         5
#   T	         7
# Example: If your program is given the String "I am a leet programmer", it should print 
# "1 4m 4 l337 pr0gr4mm3r" as the leetspeak translation

# Do this:
    # 1). get user input as input_string --> input_string = input("Let's talk LeetSpeak! Give me a message,\n and I'll give you an output: ").upper()
    # 2). create empty string --> output_string = ""
    # 3). set up for-loop to iterate through input_string --> for letter in input_string:
    # 4). create dummy character to point to char in input_string --> l = letter
    # 5). set up if statements to check for characters in chart above, within, specify that l = "leetstring"
    # 6). after last if-statement and within for-loop, output_string += l

input_string = input("Let's talk LeetSpeak! Give me a message,\n     and I'll give you an output: ").upper()
output_string = ""

for letter in input_string:
    l = letter
    if letter == "A": # these are like switches < if "...", l changes to new character in LeetSpeak
        l = "4"
    if letter == "E":
        l = "3"
    if letter == "G":
        l = "6"
    if letter == "I":
        l = "1"
    if letter == "O":
        l = "0"
    if letter == "S":
        l = "5"
    if letter == "T":
        l = "7"
    output_string += l                      # concatenates l to output_string

print(output_string)

print("\n ----- \n")

# 6. Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to 
# the length of 5.

# Examples:

# Good => Goooood 
# Cheese => Cheeeeese 
# Man => Man 
# Spoon => Spooooon 

# takes input from user
message = input("Give me a message, and I'll make your double vowels looooog!: ").lower()
print("")

# creates new string for output after manipulation of input message
output_message = ""

# loop through each character in input message and append changes to output message

index = 0

while index < len(message):
    char = message[index]
    c = char
    if index + 1 == len(message):
        output_message += c
        break
    elif char == "o" and message[index + 1] == "o":
        c = "o" * 5
        if index == len(message):
            break
        else: 
            index += 1
    elif char == "e" and message[index +1] == "e":
        c = "e" * 5
        if index == len(message):
            break
        else:
            index += 1
    elif char == "i" and message[index +1] == "i":
        c = "i" * 5
        if index == len(message):
            break
        else:
            index += 1
    elif char == "a" and message[index +1] == "a":
        c = "a" * 5
        if index == len(message):
            break
        else:
            index += 1
    elif char == "u" and message[index +1] == "u":
        c = "u" * 5
        if index == len(message):
            break
        else:
            index += 1
    output_message += c
    index += 1

print(output_message)

# I am aware this answer is way too long and complicated, but this is what I got on my own...

print("\n ----- \n")

# 7. Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of that string.

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh 
# unir yrnearq"
# hint: can use a modulus operator

alphabet = "abcdefghijklmnopqrstuvwxyz"
rot13_alpha = "nopqrstuvwxyzabcdefghijklm"

my_message = input("Let's make a secret message! \nGive me a message: ").lower()
secret_message = ""

for char in my_message:                                         # loops through message
    if char in alphabet:                                        #checks if letter is in alphabet
        secret_message += rot13_alpha[alphabet.index(char)]     # finds index of letter in alphabet and 
                                                                #concatenates cipher letter to secret_message
    else:
        secret_message += char                                  # concatenates any character other than letter to secret_message
print(f"Here is your secret message: {secret_message}")

print("\n ----- \n")
    
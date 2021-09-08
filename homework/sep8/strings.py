# # Strings
# # Learning Python Strings

# "Victoria"

# "Walker"

# "I'm a new developer"

# # escape characters allow us to use characters as we normally would within strings
# # without the program attempting to interpret the character
# 'I\'m a string and I have to escape my single quote.'

# # long strings over multiple lines can be captured between tripple quotes 
# # like """ """ or ''' '''
# """
# I am a string
# and I can span
# multiple lines!
# """

# long_string = """\tWe the People of the United States, in Order to form a more \v\v\v
# perfect Union, establish Justice, insure domestic\n Tranquility, 
# provide for the common defence, promote the general Welfare, 
# \tand secure the Blessings of Liberty to ourselves and our Posterity, 
# do ordain and establish this Constitution for the United States of 
# America."""

# print("Hello" + "World")

# print("3" + "5")

# print(3.14 * 2)

# True # 1
# False # 0
# # ref Boolean Logic for more info

# print(True + True)

# # print(long_string)


# Variables are like labels
# variable = value

first_name = "Victoria"
last_name = "Walker"

# print(first_name)
# print(last_name)
# print(first_name, last_name)
# print(last_name, first_name)
# print(first_name + " " + last_name)
# print(first_name + last_name)
# print(first_name + "     " + last_name)

# a = 8
# found_coins = 20
# magic_coins = 10
# stolen_coins = 3

# result = found_coins + magic_coins * 365 - stolen_coins * 52
# print(result)

# # String Formatting

# first_name = "Jonathan"
# last_name = "Walker"

# # Hello Jonathan Walker. How are you doing today?

# sentence = "Hello {} {}. How are you doing today?".format("Jonathan", "Walker")
# print(sentence)

# sentence2 = "Hello {} {}. How are you doing today?".format(first_name, last_name)
# print(sentence2)

# sentence3 = "Hello {0} {1}. How are you doing today?".format(first_name, last_name)
# print(sentence3)

# sentence4 = "Hello {1} {0}. How are you doing today?".format(first_name, last_name)
# print(sentence4)

# sentence5 = "Hello {first} {last}. How are you doing today?".format(first = "Jonathan", last = "Walker")
# print(sentence5)

# sentence6 = "Hello {0} {1} {1} {1}. How are you doing today?".format(first_name, last_name)
# print(sentence6)

# sentence7 = "Hello {first} {last} {last} {last}. How are you doing today?".format(first = first_name, last = last_name)
# print(sentence7)

# f-strings

param1 = 'first'
param2 = 'second'

f"Parameters {param1}:{param2}"

# first_name = "Kim"
# last_name = "Kardashian"

# sentence = f"Hello {first_name} {last_name}. How are you doing today?"
# print(sentence)

# print(type(first_name)) #str
# print(type(95)) #int
# print(type(95.91)) #float
# print(type(False)) #bool

# # isinstance() tests whether a specified object is of a specified type
# isinstance(5, int) #True
# isinstance(5, bool) # False

# print(isinstance(99, int)) # True
# print(isinstance('99', int)) # False because '99' is now a string

# print(abs(-5))
# print(pow(2,2)) # same as 2 ** 2
# print(round(5.5)) # will round up to 6

# name = input("What is your name? ")
# print(f"Your name is {name}.")

#Conditions

# True and True # True
# False and True # False
# 1 == 1 and 2 == 1 # False
# "test" == "test" # True
# 1 == 1 or 2 != 1 # True
# True and 1 == 1 # True
# False and 0 != 0 # False
# True or 1 == 1 # True
# "test" == "testing" # False
# 1 != 0 and 2 == 1 # False

# first_name = input("First name? ")
# last_name = input("Last name? ")
# print(f"Hello, My name is {first_name} {last_name}")

# # Vowel Lab
# letter = input("Please enter a letter: ")
# lower_letter = letter.lower()

# if (lower_letter == 'a' or lower_letter == 'e' or lower_letter == 'i' or lower_letter == 'o' or lower_letter == 'u'):
#     print("Vowel")
# elif lower_letter == 'y':
#     print("That's sometimes a vowel, depending on the context.")
# else:
#     print("Not Vowel")

# # While Statements

# count = 0
# while count < 10:
#     print("Victoria")
#     count += 1

# while True: 
#     answer = input("Say when: ")

#     if answer.lower() == 'when':
#         break

# print('outside of while loop')

# Write an app which asks the user for an input and then displays 
# a message indicating whether the number is even or odd.

num = ""

while num != "stop":
    num = input("Please enter a number or type 'stop': ")
    if int(num) % 2 == 0:
        print("That is an even number.")
    elif int(num) % 2 != 0:
        print("That is an odd number.")
    # elif num == "stop":
    #     print("Done!")
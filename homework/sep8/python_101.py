# Medium problems

# 1. Tip Calculator
# Your task is to write a program that calculates how much of a tip to leave at a restaurant.

# Prompt the user for two things:

# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). 
# The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%

bill_amount = input("Bill amount: ")
level_of_service = input("Was your service 'good,' 'fair,' or 'bad'? ")
if level_of_service.lower() == 'good':
    tip_amount = 0.20
elif level_of_service.lower() == 'fair':
    tip_amount = 0.15
elif level_of_service.lower() == 'bad':
    tip_amount = 0.10

tip_money = tip_amount * 100
total_amount = float(bill_amount) + tip_amount * float(bill_amount)
print(f"Your bill amount is: ${bill_amount}")
print(f"Level of service? {level_of_service}")
print(f"Your tip amount is: ${tip_money}")
print("Your total bill is: $" + "%.2f" % total_amount)

# 2. Tip Calculator 2
# Allow the ability to divide the check into a equal parts amount a number of people. The user 
# will enter the number of people to be divided amongst.

split_num = int(input("How many ways would you like to split the bill? "))
amount_per_person = (total_amount / split_num)
print("Amount per person: $" + "%.2f" % amount_per_person)

# 3. How many coins?
# Write a program that will prompt you for how many coins you want. Initially you have no coins. 
# It will ask you if you want a coin? If you type "yes", it will give you one coin, and print 
# out the current tally. If you type no, it will stop the program. 

coin_count = 0

want_coin = input("Do you want a coin? yes or no? ")

while want_coin == "yes":
    coin_count += 1
    print(f"You have {coin_count} coins")
    want_coin = input("Do you want another coin? yes or no? ")
print("All done")

# 4. Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border.

print("Let's make a box!")
height = int(input("How high? (enter a number) "))
height_counter = height - 1
width = int(input("How wide? (enter a number) "))
space = (width - 2) * " "

print("*" * (width))
while height_counter - 1 > 0:
    print (f"*{space}*")
    height_counter += -1
print("*" * (width))

# 5. Print a Triangle
# Print a triangle consisting of * characters like this:
#    *
#   ***
#  *****
# *******

# simply...

print ((" " * 3) + "*")
print ((" " * 2) + "***")
print (" " + "*****")
print("*******")

# Let's get fancy

print("Let's make a triangle! How wide would you like it to be?")
width = int(input("Enter a number: "))
space = " "
counter = 1
space_count = int((width - counter) / 2)

while (counter < width) and space_count >= 0:
    print (space * (space_count) + "*" * counter)
    counter += 2
    space_count += -1

# 6. Multiplication Table
# Print the multiplication table for numbers from 1 up to 10.

counter = 1
times = 1
while counter < 11:
    while times < 11:
        print(f"{counter} X {times} = {counter * times}")
        times += 1
    counter += 1
    times = 1


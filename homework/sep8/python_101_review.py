# 1. Tip Calculator

bill_amount = float(input("Bill amount: "))
level_of_service = input("Was your service 'good,' 'fair,' or 'bad'? ")
if level_of_service.lower() == 'good':
    tip_amount = 0.20
elif level_of_service.lower() == 'fair':
    tip_amount = 0.15
elif level_of_service.lower() == 'bad':
    tip_amount = 0.10
else:
    print("Please try again.")
    exit()

tip_money = tip_amount * bill_amount
total_amount = bill_amount + tip_money
print(f"Your bill amount is: ${bill_amount:.2f}")
print(f"Level of service? {level_of_service}")
print(f"Your tip amount is: ${tip_money:.2f}")
print(f"Your total bill is: ${total_amount:.2f}")

# 2. Tip Calculator 2

split_num = int(input("How many ways would you like to split the bill? "))
amount_per_person = (total_amount / split_num)
print(f"Amount per person: ${amount_per_person:.2f}")

print("-----") 

# 3. Coins

coins = 0 

while True: 
    print(f"You have {coins} coins.")
    another_coin = input("Do you want another? ")
    if another_coin == 'yes':
        coins += 1
    elif another_coin == 'no':
        print("Bye")
        break
    else:
        print("Invalid input, please try again")

# 4. Print a Box

# height = 4, width = 6
# num at start and end = width
# inside, number of stars = 2, number of spaces = width - 2

height = int(input("Height: "))
width = int(input("Width: "))

rows = "*" * width
columns = "*" + " " * (width - 2) + "*"
y = 0 # first row

while y < height:
    if y == 0 or y == height - 1:
        print(all_star)
    else:
        print(two_star)
    y += 1

# 5. Print a Triangle

# 3. How many coins?
# Write a program that will prompt you for how many coins you want. Initially you have no coins. 
# It will ask you if you want a coin? If you type "yes", it will give you one coin, and print 
# out the current tally. If you type no, it will stop the program. 

coins = 0 #initially you have no coins
run = 'yes' #to run the while loop

# cycle to keep asking question until they enter in something that says they don't want another coin
# need a loop to cycle
while run == 'yes':
    print("You have " + str(coins) + " coins.")
    run = input("Do you want another coin? ") #prompts user for more coins, if yes - run = 'yes'
    if run == 'yes':
        coins = coins + 1
    # else: <-- not needed :)
    #     break
    #if they enter anything other than 'yes', program will end

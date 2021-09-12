# Nine Lives Game Lab

import random

heart_symbol = u'\u2764'

# creates a list of hearts for life meter
lives = list(heart_symbol * 9)

words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]

secret_word = list(random.choice(words)) # selects random word from list and assigns to secret_word variable
# print(secret_word) # for debugging - comment this out at the end

final_word = "".join(secret_word.copy())

clue = list('?????') # question marks stored as list

print("Let's play a game! I'm thinking of a five-letter word.")

while True:
    if (len(lives) > 0) and ("?" in clue): # checks that you still have lives and there are ?s in clue list
        guess = input("Guess a letter: ") # asks for user input for a letter
        letter_found = False
        for index in range(0, len(secret_word), 1):
            if secret_word[index] == guess:
                letter_found = True
                clue[index] = guess
                print(clue)
                print(lives)
                print("correct guess")
        if not letter_found:
            del lives[-1]
            print(lives)
            print("wrong guess")
    elif "?" not in clue:
        print(f"You win! The word is {final_word}")
        break
    else:
        print("Game over. You lose!")
        break

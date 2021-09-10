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

print("\nLet's play a game! I'm thinking of a five-letter word.\n")

while True:
    if (len(lives) > 0) and ("?" in clue): # checks that you still have lives and there are ?s in clue list
        guess = input("Guess a letter: ") # asks for user input for a letter
        letter_found = False
        if guess in secret_word:
            index = 0
            while index < len(secret_word):
                if secret_word[index] == guess:
                    letter_found = True
                    clue[index] = guess
                    index += 1
                else:
                    index += 1
            print(f"\ncorrect guess! The letter '{guess}' is in my word.\n")
            print(f"Clue: {clue}")
            print(f"Lives left: {lives}\n")
            
        if not letter_found: # if user letter not found in secret_word, delete a life
            del lives[-1]
            print("Wrong guess!\n")
            print(f"Clue: {clue}")
            print(f"Lives left: {lives}\n")
    elif "?" not in clue: # if clue is out of ?'s that means they have guessed the word, and this runs
        print(f"You win! The word is {final_word}")
        break
    else:
        print("Game over. You lose!")
        break

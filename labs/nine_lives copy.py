# Nine Lives Game Lab

import random

heart_symbol = u'\u2764'

# creates a list of hearts for life meter
lives = list(heart_symbol * 9)

words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]

secret_word = list(random.choice(words)) # selects random word from list and assigns to secret_word variable
print(secret_word) # for debugging - comment this out at the end

final_word = "".join(secret_word.copy())

# secret_word = "teeth"

clue = list('?????') # question marks stored as list

print("Let's play a game! I'm thinking of a five-letter word.")

while True:
    if (len(lives) > 0) and ("?" in clue): # checks that you still have lives and there are ?s in clue list
        guess = input("Guess a letter: ") # asks for user input for a letter
        while guess in secret_word:
        # for i in len(secret_word):  <-- just in case :)
            # if secret_word.count(guess) > 1 and secret_word.count(guess) > clue.count(guess):
            #     correct_guess_letter = secret_word[secret_word.index(guess) + 1:].index(guess) + secret_word.index(guess) + 1
            # else: 
            correct_guess_letter = secret_word.index(guess) # fix this line
            clue[correct_guess_letter] = guess
            print(clue)
            print(lives)
            print("correct guess")
            break
        else: # if user does not enter letter in secret word, lose a life
            del lives[-1]
            print(lives)
            print("wrong guess")
    elif "?" not in clue:
        print(f"You win! The word is {final_word}")
        break
    else:
        print("Game over. You lose!")
        break

guessed_word_correctly = False



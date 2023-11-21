import random


word_list = ['kiwi', 'strawberry',  'mango', 'apple', 'orange' ]
users_guess = random.choice(word_list)

# This code that will continuously ask the user for a letter and validate it.

while True:
    # ask the user to guess a letter 
    guess = input("Guess a letter: ")


    










# Check if the letter guessed is a  single alphabetical character.
    if guess.isalpha() and len(guess) == 1:
        if guess in users_guess:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry the letter {guess} is not in the word. Try agian")
            
    else:
        # if the guess is not valid an error message is printed, and the loop continues.
        print("Invalid letter. Please, enter another single alphabetical character.")




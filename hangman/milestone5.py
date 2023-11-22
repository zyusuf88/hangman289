import random



class Hangman:
    def __init__(self, word_list, num_lives=5):
        # nitialise the attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
       return random.choice(self.word_list)

# Test the Hangman class
if __name__ == "__main__":
    hangman_game = Hangman(['kiwi', 'strawberry',  'mango', 'apple', 'orange' ])
    print(f"Chosen word: {hangman_game.word}")
    print(f"Word Guessed: {hangman_game.word_guessed}")
    print(f"Number of Lives: {hangman_game.num_lives}")
    print(f"Number of Letters: {hangman_game.num_letters}")
    print(f"List of Guesses: {hangman_game.list_of_guesses}")


def check_guess(self, guess):
    guess = guess.lower()
    
    if guess in self.word:
 #Print a message for a correct guess
     print(f"Good guess! {guess} is in the word.")
     for i, letter in enumerate(self.word):
        if letter == guess:
            self.word_guessed[i] = guess
        self.num_letters -= 1
    else:
        # Reduce num_lives by 1
            self.num_lives -= 1
        
            print(f"Sorry, {guess} is not in the word.")
           
            print(f"You have {self.num_lives} lives left.")



def ask_for_input(self):
        while True:
            guess = input("Guess a letter (type 'exit' to stop): ")

            # if statement that runs if the guess is NOT a single alphabetical character
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            # elif statement that checks if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:
                print(f"You've already tried the letter '{guess}'.")
            else:
                self.check_guess(guess)
                # Append the guess
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives=5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break

        # Check if num_letters is greater than 0
        elif game.num_letters > 0:
            game.ask_for_input()

        # If num_lives is not 0 and num_letters is not greater than 0, the user has won
        else:
            print('Congratulations. You won the game!')
            break


if __name__ == "__main__":
    word_list =(['kiwi', 'strawberry',  'mango', 'apple', 'orange' ])
print(f"Chosen word: {hangman_game.word}")


play_game(word_list)
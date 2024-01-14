import random


class Hangman:
    """
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    - word_list (list): List of words to be used in the game.
    - num_lives (int): Number of lives the player has.

    Attributes:
    - word (str): The word to be guessed picked randomly from the word_list.
    - word_guessed (list): A list of the letters of the word, with '_' for each letter not yet guessed.
    - num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
    - num_lives (int): The number of lives the player has.
    - list_of_guesses (list): A list of the letters that have already been tried.

    Methods:
    - choose_random_word(): Selects a random word from the word_list.
    - check_guess(guess): Checks if the guessed letter is in the word.
    - ask_for_input(): Asks the user for a letter.
    """

    def __init__(self, word_list, num_lives=5):
        # Initialize the attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            # Print a message for a correct guess
            print(f"Good guess! {guess} is in the word.")
            positions_updated = set()  # Keep track of positions already updated
            for i, letter in enumerate(self.word):
                if letter == guess and i not in positions_updated:
                    self.word_guessed[i] = guess
                    positions_updated.add(i)  # Mark the position as updated
                    self.num_letters -= 1

        else:
            # Reduce num_lives by 1
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        print(f"Current word: {' '.join(self.word_guessed)}")
        print(f"Number of letters to guess: {self.num_letters}")
        guess = input("Guess a letter: ")

        # If statement that runs if the guess is NOT a single alphabetical character
        if not (len(guess) == 1 and guess.isalpha()):
            print("Invalid letter. Please, enter a single alphabetical character.")
        # Elif statement that checks if the guess is already in the list_of_guesses
        elif guess in self.list_of_guesses:
            print(f"You've already tried the letter '{guess}'.")
        else:
            self.check_guess(guess)
            # Append the guess
            self.list_of_guesses.append(guess)

def play_game(word_list):
    """
    Play the Hangman game.

    Parameters:
    - word_list (list): List of words for the game.
    """
    # Create an instance of the Hangman class
    game = Hangman(word_list)

    # While loop to ensure the user gets no more than specified chances
    while game.num_lives > 0:
        game.ask_for_input()

         # Check if the user has guessed the full word
        if '_' not in game.word_guessed:
            print(f'Congratulations. You won the game! The word is: {game.word}')
            break
         # Check if the user has lost the game
        if game.num_lives == 0:
         print(f'Sorry, You lost! The correct word was: {game.word}')


if __name__ == "__main__":
    word_list = ['kiwi', 'grape', 'mango', 'apple', 'plum', 'peach', 'guava']
    # Call the play_game function with the word_list
    play_game(word_list)

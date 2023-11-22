import random

class Hangman:
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
        print(f"Current word: {' '.join(self.word_guessed)}")
        print(f"Number of letters: {self.num_letters}")
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
    # num_lives = 
    # game = Hangman(word_list, num_lives=5)

    # while statement to ensure the user gets no more than 5 chances
    while game.num_lives > 0:
        game.ask_for_input()

        # Check if the user has guessed all the letters
        if game.num_letters == 0:
            print('Congratulations. You won the game!')
            break
    else:
        print('Sorry, You lost!')

if __name__ == "__main__":
    word_list = ['kiwi', 'strawberry', 'mango', 'apple', 'orange']
    game = Hangman(word_list, num_lives=5)
    play_game(word_list)

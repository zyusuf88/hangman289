import random

word_list = ['kiwi', 'strawberry',  'mango', 'apple', 'orange' ]

word = random.choice(word_list)

guess = input("Enter a single word: ")
if input == 1 and input.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


print(word)
# Guess the word
import random
word_list = ["camel"]
chosen_word = random.choice(word_list)
guess = input("Try to guess the letter: ").lower()

for letter in chosen_word:
  if letter == guess:
    print("Right!")
  else:
    print("Wrong!")
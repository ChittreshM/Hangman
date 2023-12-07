import turtle 
import random

turtle.bgpic("ChristmasBG.gif")

secret_words = ["christmas", "candy cane", "snowman", "santa", "reindeer", "naughty list", "elf", "snowflake", "snowman", ]

# hangman = turtle.Turtle()

# secretInput = input("Secret Word: ")
# guessed = input("Guess: ")
# def hangman_display(guessed, secret):
#   print("Your word is", secret)
#   for i in range(len(secret)):
#     for l in range(len(guessed)):
#       if guessed[l] in secret[i]:
#         print()

# hangman_display(guessed, secretInput)

################################################################################################################################

def hangman_display(guessed, secret, incorrect_guesses):
  display = ""
  for char in secret:
      if char.lower() in guessed.lower():
          display += char
      elif char.isalpha():
          display += "_"
      else:
          display += " "
  
  if incorrect_guesses > 0:
      display += f"   (Incorrect guesses: {incorrect_guesses}/5)"
  
  return display

# Example usage:
secret_word = input("Secret Word: ")
guessed_letters = input("Guess: ")
incorrect_guesses = 0
display_result = hangman_display(guessed_letters, secret_word, incorrect_guesses)
print(display_result)
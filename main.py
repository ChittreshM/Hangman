import turtle 
import random

wn = turtle.Screen()
wn.bgpic("ChristmasBG.gif")
turtle = turtle.Turtle()
turtle.speed(0)
turtle.pensize(5)

secret_words = ["christmas", "candy cane", "snowman", "santa", "reindeer", "naughty list", "elf", "snowflake", "snowman"]
secret_letters = []

secret_word = list(secret_words[random.randint(0, len(secret_words)-1)])
# display = []
guessed_letters = ""


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

def hangman_setup():
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(20)

    # Draw the vertical pole
    turtle.goto(-150, -200)
    turtle.setheading(90)
    turtle.forward(300)

    # Draw the horizontal beam for the noose
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)

def hangman_display(guessed, secret):
  global display 
  display = ""
  for char in secret:
      if char.lower() in guessed.lower():
          display += char
      elif char.isalpha():
          display += "_"
      else:
          display += " "
  return display

# def hangman_display(guessed, secret):
#   global display 
#   for i in range(len(secret)):
#     display.append("_")
#     print(display)
#     if secret[i-1] in guessed[i-1]:
#       display[i-1] = secret[i-1]
#     elif secret[i-1].isalpha():
#         display.append("_")
#     else:
#         display.append("")
#   return display

def draw_hangman(num_mistakes):
  if num_mistakes == 1:
    turtle.penup()
    turtle.setpos(-70, 100)
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
  elif num_mistakes == 2:
    turtle.setpos(-50, -100)
    turtle.pendown()
    turtle.forward(40)
    turtle.penup()
  elif num_mistakes == 3:
    turtle.setpos(-50, -60)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(80)
    turtle.penup()
  elif num_mistakes == 4:
    turtle.setpos(-50, 20)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(40)
    turtle.penup()
  elif num_mistakes == 5:
    turtle.setpos(-50, 20)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(40)
    turtle.penup()


# Example usage:

hangman_setup()
# guessed_letters = list(input("Guess: "))
guessed_letters = input("Guess: ")
print(secret_word)
display_result = hangman_display(guessed_letters, secret_word)
print(display_result)
wn.mainloop()
# draw_hangman(mistakes)
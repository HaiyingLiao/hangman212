import random

word_list = ["apple","orange","grape","kiwi","banana"]
word = random.choice(word_list)
guess = input("enter a single letter:")

if len(guess) == 1 and guess.isalpha():
  print("Good guess!")
else:
  print("Oops! That is not a valid input.")
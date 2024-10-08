import random

word_list = ["apple","orange","grape","kiwi","banana"]
word = random.choice(word_list)

def check_guess(guess):
  guess_lower_case = guess.lower()
  if guess_lower_case in word:
    print(f"Good guess! {guess} is in the word.")
  else:
    print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
  while True:
    guess = input("enter a single letter:")
    if guess.isalpha() and len(guess)==1:
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")
  check_guess(guess)

ask_for_input()
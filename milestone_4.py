import random

class Hangman:
  def __init__(self,word_list,num_lives=5):
    self.word = random.choice(word_list)
    self.word_guessed = ["_"] * len(self.word)
    self.num_letters = len(self.word)
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses =[]

  def check_guess(self,guess):
    guess_lower_case = guess.lower()
    if guess_lower_case in self.word:
      print(f"Good guess! {guess} is in the word.")
      for index, letter in enumerate(self.word):
        if guess_lower_case == letter:
          self.word_guessed[index] = guess_lower_case
      self.num_letters -= 1
    else:
      self.num_lives -= 1
      print(f"Sorry, {guess} is not in the word.")
      print(f"You have {self.num_lives} lives left.")
  
  def ask_for_input(self):
    while True:
      guess = input("enter a single letter:")
      if not guess.isalpha() or len(guess)!=1:
        print("Invalid letter. Please, enter a single alphabetical character.")
      elif guess in self.list_of_guesses:
        print("You already tried that letter!")
      else:
        self.check_guess(guess)
        self.list_of_guesses.append(guess)
        print(self.list_of_guesses)
        print(self.word_guessed)
        print(self.word)
        print(self.num_letters)
        

word_list = ["apple", "banana", "grape", "orange"]
h =Hangman(word_list)
h.ask_for_input()
print(h.list_of_guesses)
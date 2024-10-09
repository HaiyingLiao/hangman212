# Hangman

## Project Description

Hangman is a classic word-guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters. In this project, we’ve implemented the game in Python where the computer randomly selects a word from a predefined list, and the player has to guess the word within a limited number of incorrect attempts.

The aim of the project is to practice Python programming skills by implementing basic game logic.

The project helped me enhance my understanding of string and list manipulation, using the random module, handling user input, managing control flow with loops and conditionals, and working with classes in Python.

## Installation Instructions

To run this Hangman game, follow the steps below:

1. Ensure you have Python 3 installed. If not, download and install it from [Python's official website](https://www.python.org/downloads/).
2. Clone or download the project files from this repository.

- If using Git, clone the repository:

  `git clone https://github.com/HaiyingLiao/hangman212.git`

- If downloading the project as a ZIP file, extract it after downloading.

3. Navigate to the project directory:
   `cd hangman212`
4. Install any required dependencies if applicable. However, this basic implementation doesn't require any external libraries beyond Python's standard library.

## Usage Instructions

Once the installation is complete, follow the instructions below to play the game:

1. Run the milestone_5.py file in your terminal:
   `python milestone_5.py`
2. Optionally, redefine the word_list
3. The computer will randomly select a word from the word list. The player’s objective is to guess the word one letter at a time.
4. After each guess, the game will display:

- Whether the guessed letter is in the selected word.
- Whether the letter has already been tried.
- How many lives are left.

5. If the player guesses the word correctly before running out of attempts, they win the game. If they use all their attempts, the game ends, and the correct word is revealed.

## File Structure

Hangman212/

└── hangman/
├── hangman_Template.py # task template

├── milestone_2.py # milestone tasks

├── milestone_3.py # milestone tasks

├── milestone_4.py # milestone tasks

├── milestone_5.py # Main Python script for running the game

├── README.md # Project overview and instructions

## License

MIT License

Copyright (c) 2024 Haiying Liao

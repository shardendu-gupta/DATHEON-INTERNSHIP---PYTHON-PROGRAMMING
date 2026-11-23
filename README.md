# Hangman Word Guessing Game

## Project Overview

Hangman Word Guessing Game is a simple Python-based console game where the player tries to guess a randomly selected hidden word one letter at a time.

The player gets a maximum of 6 incorrect attempts to guess the complete word. An ASCII Hangman drawing is displayed and updated after every incorrect guess.

## Features

- Random word selection using Python's `random` module.
- Hidden word display using underscores.
- Letter-by-letter guessing system.
- Tracks previously guessed letters.
- Prevents duplicate guesses and unnecessary penalties.
- Maximum 6 incorrect attempts.
- ASCII-based Hangman visual stages.
- Win and Game Over messages.
- Displays the correct word when the player loses.
- Input validation for invalid entries.


## How to Play

1. Run the Python program.
2. The computer randomly selects a word from `words.txt`.
3. The selected word is displayed as hidden underscores.
4. Enter one alphabet letter at a time.
5. Correct guesses reveal the corresponding letters.
6. Incorrect guesses update the Hangman drawing and reduce remaining attempts.
7. Avoid repeating previously guessed letters.
8. Guess the complete word within 6 incorrect attempts to win.

## Game Rules

- Only one alphabet letter can be entered at a time.
- Repeated guesses do not reduce attempts.
- Maximum incorrect attempts allowed: 6.
- Guess the complete word to win.
- If all 6 attempts are used, the game ends.


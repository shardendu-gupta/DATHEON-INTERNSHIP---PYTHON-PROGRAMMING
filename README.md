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





# Stock Portfolio Performance Tracker

## Project Overview

The Stock Portfolio Performance Tracker is a Python project developed as part of my Datheon Python Development Internship (Task 2).

This project helps users track their stock investments by calculating investment amounts, current market values, profit/loss, and percentage returns using stock prices stored in a CSV file.

## Features

- Enter multiple stock symbols.
- Add buying price and quantity for each stock.
- Read current stock prices from a CSV file.
- Calculate total investment and market value.
- Calculate individual stock profit/loss.
- Calculate percentage returns.
- Calculate overall portfolio performance.
- Export portfolio summary to a CSV file.

## Technologies Used

- Python
- CSV Module
- File Handling
- Dictionaries
- Loops and Conditional Statements

**Step 4: Enter Stock Details**

Enter the following information when prompted:

- Stock Symbol
- Buying Price
- Quantity

**Step 5: View Portfolio Report**

The program calculates the portfolio performance and automatically generates `portfolio_summary.csv`.

## Sample Stock Data

The `stock_prices.csv` file contains sample stock prices:

| Symbol | Company | Current Price |
|---|---|---:|
| AAPL | Apple | 180 |
| MSFT | Microsoft | 350 |
| GOOGL | Google | 170 |
| AMZN | Amazon | 190 |
| NVDA | Nvidia | 140 |

## Output

The program displays:

- Buying Price
- Current Price
- Quantity
- Total Investment
- Market Value
- Profit/Loss
- Return Percentage
- Overall Portfolio Performance

## Learning Outcomes

Through this project, I practiced:

- Python dictionaries and loops.
- CSV file handling.
- Reading and writing CSV files.
- Performing financial calculations.
- Working with structured data.

## Note

The stock prices included in this project are sample values for demonstration purposes and are not live market prices.

## Internship

Developed as part of the Datheon Python Development Internship – Task 2.












import random

# Load words from file
file = open("words.txt", "r")
words = file.read().splitlines()
file.close()

# Select random word
secret_word = random.choice(words).lower()

guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

# Hangman ASCII drawings
hangman_art = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("\n===== HANGMAN WORD GUESSING GAME =====")

while wrong_guesses < max_attempts:

    print(hangman_art[wrong_guesses])

    # Display hidden word
    hidden_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "

    print("Word:", hidden_word)
    print("Guessed Letters:", sorted(guessed_letters))
    print("Remaining Attempts:", max_attempts - wrong_guesses)

    # Take user input
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter!")
        continue

    # Check duplicate letter
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.add(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")

    # Check win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nWord:", secret_word)
        print("\nCONGRATULATIONS! YOU WON!")
        break

# Check lose condition
if wrong_guesses == max_attempts:
    print(hangman_art[wrong_guesses])
    print("\nGAME OVER!")
    print("Correct Word:", secret_word)

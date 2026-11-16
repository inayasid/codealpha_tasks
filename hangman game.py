
import random

# List of predefined words
words = ["python", "coding", "computer", "program", "developer"]

# Select a random word
secret_word = random.choice(words)

# Number of incorrect guesses allowed
attempts = 6

# Store guessed letters
guessed_letters = []

print("===== WELCOME TO HANGMAN GAME =====")

while attempts > 0:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect attempts left:", attempts)

    # Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        break

    # Take input from player
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThanks for playing!")

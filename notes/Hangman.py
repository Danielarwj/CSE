import random
import string
words = ["car", "lawn", "drive", "plane", "train", "folder", "box", "eight", "book", "value",
         "Are you going to Scarborough fair?"]
secret_word = "DOG"
display_list = list("*" * len(secret_word))
letter_list = list(secret_word)
guesses_left = 8
guessed_letters = []
# print(display_list)
guess = ' '
win = False
print(string.ascii_uppercase)
HIDDEN_CHAR = "_ "

while guesses_left >= 0 and not win:
    # Show/Hide Letters
    output = []
    for i in range(len(secret_word)):
        if letter_list[i] in guessed_letters:
            output.append(letter_list[i])
        else:
            output.append(HIDDEN_CHAR)
    print("".join(output))

    if guesses_left == 0 and HIDDEN_CHAR in output:
        print("You are out of guesses and still haven't guessed the word yet. Shameful. GAME OVER.")
        print("The word was: %s" % secret_word)
        quit(0)

    if " " in letter_list:
        " ".replace(" ", "")

    # Check Win Condition
    if HIDDEN_CHAR not in output:
        print("YOU WIN!!!!!!!!!!")
        print("(Jerk.)")
        win = True
        continue

    print("You have %d guesses left" % guesses_left)

    # Take in a guess
    guess = input("Guess a letter")

    if guess == " ":
        print("That is not valid. Also, Space, Really?")

    # Add guess to list
    guessed_letters.append(guess)

    if guess.swapcase() in letter_list:
        print("correct")
    # Modify Guesses Left
    if guess in secret_word:
        print("Correct")

    else:
        print("Oops. That's wrong")
        guesses_left -= 1


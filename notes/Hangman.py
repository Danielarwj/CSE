import string
import random
words = ["BEAR! RUN NOW!!", "lawn", "drive", "plane", "train", "folder", "box", "eight", "book", "value",
         "Are you going to Scarborough fair?", "We are the champions", "Hallelujah Money", "Clint Eastwood",
         "dogs"]
secret_word = random.choice(words)
display_list = list("*" * len(secret_word))
letter_list = list(secret_word)
guesses_left = 8
guessed_letters = list(string.punctuation + " ")
legal_letters = [string.ascii_uppercase, string.ascii_lowercase]
# print(display_list)
guess = ' '
win = False
print(string.ascii_uppercase)
HIDDEN_CHAR = "_ "

while guesses_left > 0 and not win:
    # Show/Hide Letters
    output = []
    for i in range(len(secret_word)):
        if letter_list[i].lower() in guessed_letters:
            output.append(letter_list[i])
        else:
            output.append("_ ")
    print("".join(output))

    print("You have %d guesses left" % guesses_left)

    # Take in a guess
    guess = input("Guess a letter").lower()

    if guess == " ":
        print("That is not valid. Also, Space, Really?")

    # Add guess to list
    guessed_letters.append(guess)

    # Modify Guesses Left
    if guess in secret_word:
        print("Correct")

    else:
        print("Oops. That's wrong")
        guesses_left -= 1
    if guesses_left == 0 and not win:
        print("You have lost! Shameful.")
        print("The word was %s" % secret_word)

    if "_" not in output and win is True:
        guesses_left = 0
        print("You have defeated me")
        print("(jerk)")

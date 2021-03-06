import string
import random
words = ["BEAR! RUN NOW!!", "lawn", "drive", "plane", "train", "folder", "box", "eight", "book", "value",
         "Are you going to Scarborough fair?", "What is two plus two?", "Clint Eastwood", "dogs"]
secret_word = random.choice(words)
display_list = list("*" * len(secret_word))
letter_list = list(secret_word)
guesses_left = 8
guessed_letters = list(string.punctuation + " ")
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

    if HIDDEN_CHAR not in output:
        print("You have defeated me ")
        print("(jerk)")
        win = True
        continue

    print("You have %d guesses left" % guesses_left)

    # Take in a guess
    guess = input("Guess a letter").lower()

    if guess == " ":
        print("That is not valid. Also, Space, Really?")

    # Add guess to list
    guessed_letters.append(guess)

    # Modify Guesses Left
    if guess.lower() in secret_word.lower():
        print("Correct")
        guesses_left += 0
    else:
        print("Oops. That's wrong")
        guesses_left -= 1
    if guesses_left == 0 and not win:
        print("You have lost! Shameful.")
        print("The word was %s" % secret_word)

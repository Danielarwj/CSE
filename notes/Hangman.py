import random
words = ["car", "lawn", "drive", "plane", "train", "folder", "box", "eight", "book", "value",
         "Are you going to Scarborough fair?"]
secret_word = random.choice(words)
disp_list = list("*" * len(secret_word))
letter_list = list(secret_word)
guesses_left = 8
guessed_letters = []
# print(disp_list)
guess = ' '

while guesses_left > 0 and "*" in disp_list:
    # Show/Hide Letters
    output = []
    for i in range(len(secret_word)):
        if letter_list[i] in guessed_letters:
            output.append(letter_list[i])
        else:
            output.append("_ ")
    print("".join(output))

    print("You have %d guesses left" % guesses_left)

    # Take in a guess
    guess = input("Guess a letter")

    # Add guess to list
    guessed_letters.append(guess)

    # Modify Guesses Left
    if guess in secret_word:
        print("Correct")
    else:
        print("Oops. That's wrong")
        guesses_left -= 1
    if guesses_left == 0 and "*" in disp_list:
        print("You are out of guesses and still haven't guessed the word yet. Shameful. GAME OVER.")

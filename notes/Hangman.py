import random
words = ["car", "lawn", "drive", "plane", "train", "folder", "box", "eight", "book", "value",
         "Are you going to Scarborough fair?"]
secret_word = random.choice(words)
disp_list = list("*" * len(secret_word))
letter_list = [list(secret_word)]
guesses_left = 8
# print(disp_list)

while guesses_left > 0 and "*" in disp_list:
    print(''.join(disp_list))
    print("You have %d guesses left" % guesses_left)
    guess = input("Guess a letter")
    if guess in secret_word:
        print("Correct")
    else:
        print("Oops. That's wrong")
        guesses_left -= 1
    if guesses_left == 0 and "*" in disp_list:
        print("You are out of guesses and still haven't guessed the word yet. Shameful. GAME OVER.")





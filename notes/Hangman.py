import random
words = ["car", "lawn", "drive", "plane", "train", "folder", "box", "eight", "book", "value"]
secret_word = random.choice(words)
disp_list = ["*" * len(secret_word)]
letter_list = [list(secret_word)]
guesses_left = 5

while guesses_left > 0 and "*"in disp_list:
    print(''.join(disp_list))
    print("You have %d guesses left" % guesses_left)
    guess = input("Guess a letter")

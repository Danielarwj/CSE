import random
number = random.randint(0, 100)
guesses = 5

while guesses > 0:
    print("Guess a Number between one and 20")
    guess = int(input())

    guesses = guesses-1
    if guesses = 0 and guess > number:
        print("You didn't guess it. Game Over")
    if guess < number:
        print("Guess is too low")
    elif guess > number:
        print("Guess is too high")
    if guess == number:
        print("Correct. Game Over")
        guesses = 0

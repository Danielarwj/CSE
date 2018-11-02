import random
number = random.randint(0, 20)
guesses = 5

while guesses > 0:
    print("Guess a Number between one and 20")
    guess = int(input())

    guesses = guesses-1

    if guess < number:
        print("Guess is too low")
    elif guess > number:
        print("Guess is too high")
    if guess == number:
        print("Correct. Game Over")
    elif guesses == 0:
        print("You didn't guess it. Game Over")

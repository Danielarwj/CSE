import random
number = random.randint(0, 200)
print(number)


guesses = 5


while guesses < 6:
    print("Insert Number")
    guess = input()

    if guess <= number:
        print("Guess is too low")
    if guess > number:
        print("Guess is too high")
    if guess == number:
        print("Correct")










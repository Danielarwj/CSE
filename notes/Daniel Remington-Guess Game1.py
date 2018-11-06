import random
guesses = 5
playing = True
play_again = True
print("Instructions: You have 5 guesses to guess a number.")
print("The range of numbers is based on your difficulty")
print("Remember to put use a space before you type in your difficulty")
difficulty = input("Choose your difficulty-Easy or Impossible")
if difficulty == " Easy":
    number = random.randint(1, 20)
    print("Your numbers are between 0 and 20")
    guess = int(input("Guess a number"))
else:
    number = random.randint(1, 1000)
    print("Your numbers are between one and 1000")
    guess = int(input("Guess a number"))

while guesses != 0 and playing:

    if guess < number:
        print("Guess is too low")
        guess = int(input("Try Again"))
        guesses = guesses - 1
    elif guess > number:
        print("Guess is too high")
        guess = int(input("Try Again"))
        guesses = guesses - 1
    if guess == number:
        print("Correct. Game Over")
        guesses = 0
        playing = False

if guesses == 0 and guess != number:
    print("You didn't guess it! Game Over.")
    print("The number was %i" % number)

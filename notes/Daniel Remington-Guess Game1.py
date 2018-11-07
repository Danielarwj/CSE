import random
guesses = 4
playing = True
print("Instructions: You have 5 guesses to guess a number.")
print("The range of numbers is based on your difficulty")
print("Remember to put use a space before you type in your difficulty")
difficulty = input("Choose your difficulty-Easy or Impossible")
if difficulty == " Easy":
    number = random.randint(1, 20)
    print("Your numbers are between 0 and 20")
else:
    number = random.randint(1, 1000)
    print("Your numbers are between one and 1000")
guess = int(input("Guess a number"))

while guesses > 0 and playing:
    if guess < number:
        print("Guess is too low")
    elif guess > number:
        print("Guess is too high")
    if guess == number:
        print("Correct. Game Over")
        guesses = 0
        playing = False
    else:
        guess = int(input("Try Again "))
        guesses -= 1

if guesses == 0 and guess != number:
    print("You didn't guess it! Game Over.")
    print("The number was %i" % number)

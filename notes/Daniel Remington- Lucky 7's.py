import random
amount = 15
print("Welcome to Lucky 7's. Here is the game where you constantly try to 'keep' your money")
bet = 1
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
roll = dice1+dice2
rounds = ("It took you %s to lose all of your money" % )

while amount > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll = dice1+dice2
    print("You rolled a " + str(roll))

    if roll == 7:
        amount += 4
        print("Your amount is " + str(amount))
        print("Congratulations, you won 4 dollars!")

    else:
        amount -= 1
        print("Your amount is " + str(amount))
        print("Oops, sorry. Why don't you roll again")

print("Sorry. You lost all your money.")

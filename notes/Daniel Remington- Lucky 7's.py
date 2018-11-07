import random
starting_amount = 15
print("Welcome to Lucky 7's. Here is the game where you constantly try to 'keep' your money")
bet = 1
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
roll = dice1+dice2
print(roll)

while starting_amount > 0:
    if roll == 7:
        starting_amount += 4
        print(starting_amount)
    else:
        starting_amount -= 1
        print(starting_amount)
        print("Oops, sorry. Why don't you roll again")


if starting_amount == 0:
    print("Sorry. You lost all your money.")







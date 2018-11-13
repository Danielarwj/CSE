import random
amount = 15
print("Welcome to Lucky 7's. Here is the game where you constantly try to 'keep' your money")
bet = 1
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
roll = dice1+dice2
rounds = 0


while amount > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll = dice1+dice2
    print("You rolled a " + str(roll))
    rounds += 1
    if roll == 7:
        amount += 4
        print("Congratulations, you won 4 dollars!")

    else:
        amount -= 1
        print("Oops, sorry. Why don't you roll again")
    print("Your amount is " + str(amount))

    if amount == amount >  :
        maximum_money = amount


print("Sorry. You lost all your money.")
print("Wow, It took you %s rounds to lose all your money!. Impressive" % rounds)
print (maximum_money)
import math
# challenge 10 is the datetime
import datetime
datetime.datetime.now()
datetime.datetime(2018, 12, 4, 9, 17, 20)
print(datetime.datetime.now())

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
y_potential_vowel = "y"

# Challenge 9


def challenge_one(letter):
    if letter in vowels:
        print("%s is a vowel" % letter)
    if letter in consonants:
        print("%s is a consonant" % letter)
    elif letter in y_potential_vowel:
        print("%s is both a consonant and a vowel. Strange." % letter)


challenge_one("r")

# Challenge 11


def challenge_three(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


print(challenge_three(5))


# Challenge 12


def challenge_four(number_1, number_2):
    return math.gcd(number_1, number_2)


print(challenge_four(4, 8))

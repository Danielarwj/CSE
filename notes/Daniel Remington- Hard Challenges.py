# challenge two is the datetime
import datetime
datetime.datetime.now()
datetime.datetime(2018, 12, 4, 9, 17, 20)
print(datetime.datetime.now())

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
y_potential_vowel = "y"


def challenge_one(letter):
    if letter in vowels:
        print("%s is a vowel" % letter)
    if letter in consonants:
        print("%s is a consonant" % letter)
    elif letter in y_potential_vowel:
        print("%s is both a consonant and a vowel. Strange." % letter)


challenge_one("r")


def challenge_three(string):
    if string == int:
        print("Your string,%d, is an integer" % string)
    else:
        print("Your string,%s, is not an integer" % string)


challenge_three(200)

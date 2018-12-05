# This is challenge 5
def challenge1(radius):
    return 3.14*(radius**2)


print(challenge1(1.1))

# This is challenge 6


def challenge2(radius):
    return(4/3)*(3.14*(radius**3))


print(challenge2(5))

# This is challenge 7


def challenge3(number):
    return number+(number+number)+(number+number+number)


print(challenge3(2))

# This is challenge 8


def challenge4(number):
    if number < 1850:
        print("%d is not within 150 of 2000" % number)
    elif number > 2150:
        print("%d is not within 150 of 2000" % number)
    elif number >= 1850:
        print("%d is within 150 of 2000" % number)
    elif number <= 2150:
        print("%d is within 150 of 2000" % number)


challenge4(2150)

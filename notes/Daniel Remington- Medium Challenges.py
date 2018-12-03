def challenge1(radius):
    return 3.14*(radius**2)


print(challenge1(1.1))


def challenge2(radius):
    return(4/3)*(3.14*(radius**3))


print(challenge2(5))


def challenge3(number):
    return number+(number+number)+(number+number+number)


print(challenge3(2))

def challege4(number):
    if number < 1850:
        print("%d is not within 150 of 2000")
    elif number > 2150:
        print("%d is not within 150 of 2000")
    elif number >= 1850 and <= 2150:
        print("%d is within 150 of 2000")


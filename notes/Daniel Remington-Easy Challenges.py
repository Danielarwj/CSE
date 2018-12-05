# This is challenge one


def challenge1(first_name, last_name):
    print(last_name, " ", first_name)


challenge1("John", "Doe")

# This is challenge two


def challenge2(number):
    if number % 2 == 0:
        print("%d is even" % number)
    else:
        print("%d is odd" % number)


challenge2(25)

# This is Challenge three


def challenge_three(a, b):
    return(a*b)*(1/2)


print(challenge_three(3, 4))

# This is challenge 4


def challenge4(number):
    if number < 0:
        print("%d is negative" % number)
    elif number > 0:
        print("%d is positive" % number)
    elif number == 0:
        print("%d is 0" % number)


challenge4(8)

def challenge1(first_name, last_name):
    print(last_name, " ", first_name)


challenge1("John", "Doe")


def challenge2(number):
    if number % 2 == 0:
        print("%d is even" % number)
    else:
        print("%d is odd" % number)


challenge2(25)


def area_of_triangle(a, b):
    return(a*b)*(1/2)


print(area_of_triangle(3,4))


def challenge4(number):
    if number < 0:
        print("%d is negative" % number)
    elif number > 0:
        print("%d is positive" % number)
    elif number == 0:
        print("%d is 0" % number)


challenge4(8)

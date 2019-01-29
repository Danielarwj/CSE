
"""
Objects have two main characteristics: Attributes and behavior.
The object parrot has the name,age,and color as attributes and dancing and singing as behavioral patterns
"""

"""
The term DRY- Don't Repeat Yourself- is used widely with OOP programming
OOP follows some very basic concepts:
Inheritance- The process of using details from a new class without modifying the existing class
Encapsulation- Hiding the private details of a class from other objects
Polymorphism- A concept of using common operation in different ways for different data input
"""

"""
A class is the blueprint for an object
We can think of class as an sketch of a parrot with labels. It contains all the details about the name, colors, size etc
Based on these descriptions, we can study about the parrot. Here, parrot is an object

"""


class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


def sing(self, song):
    return "{} sings {}".format(self.name, song)


def dance(self):
    return "{} is now dancing".format(self.name)


# instantiate the object
blu = Parrot("Blu", 10)

#
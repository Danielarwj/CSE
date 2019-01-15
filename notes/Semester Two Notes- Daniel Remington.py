import string
print("Hello World")

# This is a single line comment

cars = 5

driving = True

print("I have %d cars" % cars)
print("I have " + str(cars) + " cars")

age = input("How old are you")
print("How my gosh! You are %s years old. I'm not even that old!" % age)
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]

colors.append("Cyan")

print(colors)

# .Pop removes indexes and you don't know what you are deleting
# .remove removes objects and you know what you are deleting with .remove

colors.pop(0)
print(colors)

print(colors[2])

print(len(colors))

print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)
str.append(string.punctuation, " ")






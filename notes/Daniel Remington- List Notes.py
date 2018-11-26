# empty list
my_list = {}

# list of integers

# list with mixed data_types
my_random_list = {1, "Hello", 3.4}

"""
These are all examples of the different types of normal lists you could have
"""

my_number_list = ['p', 'p', 'p']
del my_number_list[1]
print(my_number_list)

print(my_number_list)

"""
odd = [1, 9]
odd.insert(1,3)
print(odd)
"""

colors = ["blue", "turquoise", "pink", "orange", "black", "red", "green", "purple", "cyan", "magenta"]
# USE SQUARE BRACKETS
print(colors)
print(colors[1])
print(colors[0])

# Length of the list
print("There are %d things in the list" % len(colors))


# Changing elements in a list
del colors[1]
print(colors)

colors[1] = "eggshell white"
print(colors)

# Looping through lists
for items in colors:
    print(items)


"""
1. Make a list
2. Change the 3rd thing in the list
3. Print the Item
4. Print the full list
"""

Star_Trek_Characters = ["Kirk", "Spock", "General U.", "Bones"]
Star_Trek_Characters[2] ="Kahn"

for item in Star_Trek_Characters:
    print(item)

print(Star_Trek_Characters)





































































































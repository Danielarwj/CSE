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

Star_Trek_Characters = ["Kirk", "Spock", "General U.", "Bones", "Picard", "Data", "Lore"]
Star_Trek_Characters[2] = "Kahn"

for item in Star_Trek_Characters:
    print(item)

print(Star_Trek_Characters)
print("The last thing in the list is %s" % Star_Trek_Characters[6])
print("The last thing in the list is %s" % Star_Trek_Characters[len(Star_Trek_Characters)-1])


# Slicing a list
print(Star_Trek_Characters[1:3])
# Includes first index and second index but not third index


print(Star_Trek_Characters[1:])
print(Star_Trek_Characters[0:4])
print(Star_Trek_Characters[1:4])


food_list = ["Turkey", "Sweet Potato Casserole", "Eggs", "Squash", "Carrot", "Chocolate Cake", "Bacon",
             "Chocolate covered Bacon","Salad",
         "Bacon with extra fat", "chicken", "Fourth of July Cookies"," Peanut Butter and Chocolate Cookies",
            "Apple Pie",
            "Roasted Salmon", "Sushi", "Poke", "Noodles", "Saltine Crackers", "Celery", "Eggplant Parm","Enchilada"]
print(len(food_list))

food_list.append("Bacon")
food_list.append("Eggs")

# Notice that everything is object.method(parameters)
print(food_list)

food_list.insert(1, "eggo waffles")
print(food_list)

food_list.remove("Salad")
print(food_list)


"""
1.Make a new list with three items
2.Add fourth item
3. Remove one of first three items
"""

Star_Wars_Characters = ["Luke", "Han", "Chewie"]

Star_Wars_Characters.insert(3, "Darth Vader")
print(Star_Wars_Characters)
Star_Wars_Characters.remove("Luke")
print(Star_Wars_Characters)


# Tuples
brands = ("apple", "samsung", "HTC") # Notice the ()'s
print(food_list)
food_list.pop(0)
print(food_list)


print(food_list.index("chicken"))

string1 = "TURQUOISE"
list1 = list(string1)
print(list1)

print("".join(list1))

for i in range(len(list1)):  # i goes through all indices
    if list1[i] == "u":  # if we find a U
        list1.pop(i)  # remove the i-th index
        list1.insert(i, "*")  # put a * there instead

"""
for character in list1:
    if character == "u:
        # replace with a*
        current index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*"
"""





















































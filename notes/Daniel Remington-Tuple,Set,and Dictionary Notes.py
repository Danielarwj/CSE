tuple1 = ("apple", "banana", "cherry")

this_set = {"pie", "cake", "cookie"}
print(this_set)

for x in this_set:
    print(x)
print("pie" in this_set)

this_set.add("orange")
print(this_set)

this_set.update(["mango", "pineapple", "grapefruit"])
print(this_set)

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)

x = this_dict.get("model")
print(x)


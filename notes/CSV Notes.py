import csv

def validate(num: str):
    if not sixteen_digits(num):
        return False
    first_num = int(num[0])
    if first_num % 2 == 0 and first_num % 3 == 0:
        return True
    return False


def sixteen_digits(num: str):
    total_num = len(num)
    if total_num == 16:
        return True
    return False


def reverse(string):
    print(string[0:9:2])
    return string[::-1]


print(reverse("Hello World"))


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        print("Writing file .......")
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        for row in reader:
            old_number = row[0]

            if validate(old_number):
                writer.writerow(row)
            # print(int(old_number) +1)
            # print(old_number)

print("OK")


# with open("Book1.csv", "r") as old_csv:
#   with open("MyNewFile.csv", "w", newline='') as new_csv:
#      print("Writing file .......")
#     writer = csv.writer(new_csv)
#    reader = csv.reader(old_csv)
#   for row in reader:
#      old_number = int(row[0])
#     new_number = old_number + 1
#    row[0] = new_number
#   writer.writerow(row)
# print(int(old_number) +1)
# print(old_number)

# print("OK")


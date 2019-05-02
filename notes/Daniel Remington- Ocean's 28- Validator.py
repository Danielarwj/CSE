# import math

import csv


def validate_card_number(num: str):
    if not sixteen_digits(num):
        return False
    last_num = int(num[15])

    list_num = list(num)
    list_num.pop(last_num)
    for index in range(len(list_num)):
        list.reverse(list_num)
        list_num[index] = int(list_num[index])
        if index % 2 == 0:
            list_num[index] *= 2
            if list_num[index] > 9:
                list_num[index] -= 9
    list_num_sum = sum(list_num)
    if list_num_sum % 10 == last_num:
        print("This is a real number! We're in, boys!: %d" % int(num))
        return True
    else:
        print("This is a false number; %d" % int(num))
        return False


# list_num = list(num)
# for index in range(len(list_num)):
# list_num[index] = int(list_num[index])


def sixteen_digits(num: str):
    return len(num) == 16


def reverse(string):
    return string[::-1]


validate_card_number(str(1707909249311050))

with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        print("Writing file .......")
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        for row in reader:
            old_number = row[0]

            if not validate_card_number(old_number):
                writer.writerow(row)
            # print(int(old_number) +1)
            # print(old_number)

print("OK")

with open("Book1.csv", "r") as old_csv:
    with open("We're_in_with_these_ones_boys.csv", "w", newline='') as new_csv:
        print("Writing file .......")
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        for row in reader:
            old_number = row[0]

            if validate_card_number(old_number):
                writer.writerow(row)
            # print(int(old_number) +1)
            # print(old_number)

print("OK")

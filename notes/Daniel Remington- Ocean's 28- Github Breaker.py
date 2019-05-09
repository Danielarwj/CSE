import csv


def officesupplies(aspect):
    if aspect == "Office Supplies":
        print(aspect)


def total_profit(num):
    profit_list.append(num)

with open("SalesInformation.csv", "r") as old_csv:
    with open("SalesFile.csv", "w", newline='') as new_csv:
        print("Hacking into the mainframe... getting those country names... I'ma gettin' them boys.")
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        office_list = []
        cosmetics_list = []
        baby_food_list = []
        snacks_list = []
        cereal_list = []
        vegetables_list = []
        household_list = []
        beverages_list = []
        meat_list = []
        personal_list = []
        clothes_list = []
        fruits_list = []
        profit_list = []

        for row in reader:
            old_number = row[2]
            profit = float(row[13])
            print(old_number)
            if old_number == "Office Supplies":
                office_list.append(old_number)
                profit_list.append(total_profit(profit))
            if old_number == "Cosmetics":
                cosmetics_list.append(old_number)
            if old_number == "Baby Food":
                baby_food_list.append(old_number)
            if old_number == "Beverages":
                beverages_list.append(old_number)
            if old_number == "Cereal":
                cereal_list.append(old_number)
            if old_number == "Household":
                household_list.append(old_number)
            if old_number == "Vegetables":
                vegetables_list.append(old_number)
            if old_number == "Meat":
                meat_list.append(old_number)
            if old_number == "Fruits":
                fruits_list.append(old_number)
            if old_number == "Clothes":
                clothes_list.append(old_number)
            if old_number == "Snacks":
                snacks_list.append(old_number)
            if old_number == "Personal Care":
                personal_list.append(old_number)


print(len(office_list))
print(len(clothes_list))
print(len(fruits_list))
print(len(personal_list))

print(sum(profit_list))

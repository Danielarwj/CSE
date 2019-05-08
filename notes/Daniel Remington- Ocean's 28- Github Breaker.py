import csv

def OfficeSupplies(aspect):
    if aspect == "Office Supplies":
        print(aspect)



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
        types_of_items = {
        }

        for row in reader:
            old_number = row[2]
            print(old_number)
            if old_number == "Office Supplies":
                office_list.append(old_number)
            # if old_number == "Fruits":
            #     old_number.append(fruits_list)
            # if old_number == "Beverages":
            #     old_number.append(beverages_list)
            # if old_number == "Personal Care":
            #     old_number.append(personal_list)

print(office_list)



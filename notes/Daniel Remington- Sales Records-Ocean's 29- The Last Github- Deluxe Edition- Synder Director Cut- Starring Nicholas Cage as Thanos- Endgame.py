import csv

items = {}

averages = {}

with open("Sales Records.csv", "r") as old_csv:
    print(" ")
    print("Mutants and humans. They have long struggled to coexist. While some try to unite the world, others try to "
          "dominate it.")
    print(" ")
    print("Neither strategy has prevailed. But when conflicts reach an impasse, inevitably something "
          "happens to shift the balance forever.")

    high_total_key = "Wiebe"
    high_total = 0
    reader = csv.reader(old_csv)
    for row in reader:
        if row[0] == 'Region':
            continue
        item_type = row[2]
        profit = float(row[13])
        units_sold = float(row[8])
        unit_price = row[9]
        unit_cost = row[10]

        try:
            items[item_type] += profit
        except KeyError:
            items[item_type] = profit

        for item in items.items():
            try:
                averages[item_type] = profit / units_sold
            except KeyError:
                averages[item_type] = profit


for key, item in items.items():
    if item > high_total:
        high_total = item
        high_total_key = key
        print(high_total_key)
    print(key, end=": ")
    print("${:,}".format(round(item, 2)))

print(averages)
print("The Keep The Koala Chlamydiah Community found that %s was the most profitable product" % high_total_key)

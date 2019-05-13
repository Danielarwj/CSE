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
    print(key, end=": ")
    print("${:,}".format(round(item, 2)))
print(averages)

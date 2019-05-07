import csv

with open("Book1.csv", "r") as old_csv:
    with open("SalesFile.csv", "w", newline='') as new_csv:
        print("Hacking into the mainframe... getting those country names... I'ma gettin' them boys.")
        writer = csv.writer(new_csv)
        reader = csv.reader(old_csv)
        for row in reader:
            old_number = row[2]
            print(old_number)
            print("WE GOT 'EM")



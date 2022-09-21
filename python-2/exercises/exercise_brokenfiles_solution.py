import csv

common_names = []
latin_names = []

with open("plants.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        common_names.append(row[1])
        latin_names.append(row[2])

books = [
    ["Wild Seed", 1980],
    ["Mind of My Mind", 1977],
    ["Clay's Ark", 1984],
    ["Patternmaster", 1976]
]
with open("books.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(books)
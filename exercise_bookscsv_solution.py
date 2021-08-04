import csv

books = [
    ["Wild Seed", 1980],
    ["Mind of My Mind", 1977],
    ["Clay's Ark", 1984],
    ["Patternmaster", 1976]
]
# Open a new file called books.csv in write mode
# Use CSVwriter to write the nested list into the file

with open("books.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(books)
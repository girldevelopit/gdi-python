import csv


common_names = []
latin_names = []
# Implement the pseudocode:
# Open the plants.csv file
# Use the CSV reader to read each row
# Append the plant's common name to common_names
# Append the plant's latin name to latin_names

with open("plants.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        common_names.append(row[1])
        latin_names.append(row[2])
"""
Complete store_grocery_list2 function which takes two arguments,
a nested list of grocery items/quantities and a filename, and writes the list into the file, separated by new lines.
Each line in the file should contain the lowercased item name
followed by the item quantity.
"""
def store_grocery_list2(groceries, filename):
  """
  >>> # For sake of tests, make sure file exists:
  >>> open('grocery.txt', mode='w').close()
  >>> store_grocery_list2([['Apples', 3], ['Bananas', 5], ['Oatmeal', 1]], 'grocery.txt')
  >>> # Now we read the file to check the results :
  >>> grocery_file = open('grocery.txt')
  >>> groceries = grocery_file.read()
  >>> groceries.strip()
  'apples (3)\\nbananas (5)\\noatmeal (1)'
  >>> grocery_file.close()
  """
  with open(filename, "w") as file:
    for grocery in groceries:
        file.write(f"{grocery[0].lower()} ({grocery[1]})\n")

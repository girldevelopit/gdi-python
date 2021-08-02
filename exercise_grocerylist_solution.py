"""
Complete store_grocery_list function which takes two arguments,
a list of grocery items and a filename, and writes the list
into the file, separated by new lines, all lowercased.
"""
def store_grocery_list(groceries, filename):
  """
  >>> store_grocery_list(['Apples', 'Bananas', 'Oatmeal'], 'grocery.txt')
  >>> # Now we read the file to check the results :
  >>> grocery_file = open('grocery.txt')
  >>> groceries = grocery_file.read()
  >>> groceries.strip()
  'apples\\nbananas\\noatmeal'
  >>> grocery_file.close()
  """
  with open(filename, "w") as file:
    for grocery in groceries:
        file.write(grocery.lower() + "\n")

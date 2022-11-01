"""
This function returns a string
with all the contents of the list
concatenated together."""
def concatenator(items):
  # Initialize a variable to empty string
  # Iterate through the list
  # Concatenate each item to the variable
  # Return the variable
  concatted = ''
  for item in items:
    concatted += item
  return concatted

# Should store "Supercalifragilisticexpialidocious"
res1 = concatenator(["Super", "cali", "fragilistic", "expialidocious"])

# Should store "fingerspitzengefühl"
res2 = concatenator(["finger", "spitzen", "gefühl"])

# Should store "nonetheless"
res3 = concatenator(["none", "the", "less"])

"""
Complete file_words function which takes a single argument,
the name of a file, and returns a list of all the words in a file,
assuming the words are separated by spaces in the file.
"""
def file_words(filename):
  """
  >>> file_words('ingredients.txt')
  ['peanut', 'butter', 'jelly', 'time']
  >>> file_words('names.txt')
  ['keira', 'rane', 'blake']
  """
  with open(filename, mode="r") as my_file:
    file_contents = my_file.read()
  return file_contents.strip().split(' ')
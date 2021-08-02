"""
Complete clean_file function which takes a single argument,
the name of a file, and returns a cleaned up version of the file
contents. The cleaned up version should be all lowercase
and have no leading or trailing whitespace.
"""
def clean_file(filename):
  """
  >>> clean_file('file.txt')
  'roasted butternut squash'
  >>> clean_file('file_funkycaps.txt')
  'farro platter'
  >>> clean_file('file_spaced.txt')
  'sweet potato burrito'
  """
  with open(filename, mode="r") as file:
    file_contents = file.read()
  return file_contents.lower().strip()
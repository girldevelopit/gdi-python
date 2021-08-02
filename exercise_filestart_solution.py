"""
Complete file_start function which takes a single argument,
the name of a file, and returns the first 30 characters of the file.
"""
def file_start(filename):
  """
  >>> file_start('cat_ipsum.txt')
  'Where is it? i saw that bird i'
  >>> file_start('hipster_ipsum.txt')
  'Brooklyn air plant activated c'
  >>> file_start('sagan_ipsum.txt')
  'Stirred by starlight Vangelis '
  >>> file_start('vegan_ipsum.txt')
  'Veggie burgers fresh peanut bu'
  """
  with open(filename, mode="r") as file:
    file_contents = file.read()
  return file_contents[0:30]
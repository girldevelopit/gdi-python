# Fix up the following function per the docstring and doctests.

def get_index(values, target_value):
  """Returns the index of a value in a list, or -1 if not found.

  >>> get_index([5, 6, 7], 8)
  -1
  >>> get_index([5, 6, 7], 7)
  2
  >>> get_index([5, 6, 7], 6)
  1
  >>> get_index([5, 6, 7], 5)
  0
  """
  found_index = -1
  index = 0

  for element in values:
    if element == target_value:
      found_index = index
    index += 1
  return found_index
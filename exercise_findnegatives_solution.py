# Complete this function to make the doctests pass,
# using the built-in map or filter function when needed.
# You may want to write an additional function
# to pass into the map or filter function.

def find_negative_temps(temps):
  """ Returns a new list with just the negative temperatures from temps.

  >>> find_negative_temps([-13, 45, -1, 0, 23])
  [-13, -1]
  >>> find_negative_temps([])
  []
  >>> find_negative_temps([23, 36, 21])
  []
  >>> find_negative_temps([-30, -60, -10])
  [-30, -60, -10]
  """

  # Python allows function definitions inside other funcs
  def is_negative(temp):
    return temp < 0

  return list(filter(is_negative, temps))
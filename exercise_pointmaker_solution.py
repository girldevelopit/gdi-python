""" This function returns a list with the two arguments."""
def make_point(x, y):
  return [round(x), round(y)]

pt1 = make_point(30, 75) # Should return [30, 75]
pt2 = make_point(-1, -2) # Should return [-1, -2]

# Bonus: Round the x and y in the list
bonus_pt = make_point(12.32, 74.11) # Should return [12, 74]
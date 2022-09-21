""" This function takes an input of a 2-dimensional list of numbers
and returns true if any of the rows add up to 15."""
def contains_15row(grid):
  # Iterate through the grid
  # Initialize a sum to 0
  # Iterate through the row
  # Add current value to sum
  # If sum is 15, return true
  # return false otherwise
  for row in grid:
    sum = 0
    for value in row:
      sum += value
    if sum == 15:
      return True
  return False



grid1 = [
  [5, 1, 6],   # 12
  [10, 4, 1],  # 15!!
  [8, 3, 2]    # 13
]
does_contain = contains_15row(grid1)

grid2 = [
  [15, 1, 6], # 22
  [10, 4, 0], # 14
  [8, 3, 2]   # 13
]
doesnt_contain = contains_15row(grid2)

""" This function takes an input of a 2-dimensional list of numbers
and returns the sum of all the numbers."""
def sum_grid(grid):
  # Initialize a sum to 0
  # Iterate through the grid
  # Iterate through current row
  # Add current value to sum
  # Return sum
  sum = 0
  for row in grid:
    for value in row:
      sum += value
  return sum

grid1 = [
  [5, 1, 6],   # 12
  [10, 4, 1],  # 15
  [8, 3, 2]    # 13
]
sum1 = sum_grid(grid1) # Should be 40

grid2 = [
  [15, 1, 6], # 22
  [10, 4, 0], # 14
  [8, 3, 2]   # 13
]
sum2 = sum_grid(grid2) # Should be 49

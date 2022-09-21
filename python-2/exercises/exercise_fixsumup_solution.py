# Fix up the following function per the docstring and doctests.

def sum_up_numbers(nums):
  """
  Sums up all the numbers in a list.

  >>> sum_up_numbers([1, 2, 3])
  6
  >>> sum_up_numbers([10, 20, 30])
  60
  """
  num_sum = 0
  for num in nums:
    num_sum += num
  return num_sum
# Fix up the following function per the docstring and doctests.

def count_positive(nums):
  """
  Returns the number of positive numbers in a list.

  >>> count_positive([2, 3, 3])
  3
  >>> count_positive([2, -1, 3])
  2
  >>> count_positive([0, -1, 3])
  1
  """
  count = 0
  for num in nums:
    if num >= 0:
      count += num + 1
  return count

# Fix the code so that the doctests pass!

def sum_of_numbers(end):
  """
  >>> sum_of_numbers(10)
  55
  """
  result = 0
  counter = 1
  while counter <= end:
    result += counter
    counter += 1
  return result

def sum_multiples(start, end, divisor):
  """
  >>> sum_multiples(1, 12, 4)
  24
  >>> sum_multiples(1, 12, 3)
  30
  """
  result = 0
  counter = start
  while counter <= end:
    if counter % divisor == 0:
      result += counter
    counter += 1
  return result


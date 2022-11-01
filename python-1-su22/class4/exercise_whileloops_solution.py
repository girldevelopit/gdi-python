def count_evens(start, end):
  counter = start
  num_evens = 0
  while counter <= end:
    if counter % 2 == 0:
      num_evens += 1
    counter += 1
  return num_evens

def count_multiples(start, end, divisor):
  counter = start
  num_multiples = 0
  while counter <= end:
    if counter % divisor == 0:
      num_multiples += 1
    counter += 1
  return num_multiples

def sum_multiples(start, end, divisor):
  sum = 0
  counter = start
  while counter <= end:
    if counter % divisor == 0:
      sum += counter
    counter += 1
  return sum

def product_of_numbers(end):
  result = 1
  counter = 1
  while counter <= end:
    result *= counter
    counter += 1
  return result
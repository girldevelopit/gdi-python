"""
Complete the fuzzbuzz function, which takes a single argument, a  number. The function should return "fuzz" if the number is divisible by 3, "buzz" if the number is divisible by 5, "fuzzbuzz" if the number is divisible by both 3 and 5, and otherwise return the number."""
def fuzzbuzz(num):
  """
  >>> fuzzbuzz(4)
  4
  >>> fuzzbuzz(3)
  'fuzz'
  >>> fuzzbuzz(5)
  'buzz'
  >>> fuzzbuzz(9)
  'fuzz'
  >>> fuzzbuzz(10)
  'buzz'
  >>> fuzzbuzz(15)
  'fuzzbuzz'
  """
  if num % 3 == 0 and num % 5 == 0:
    return 'fuzzbuzz'
  elif num % 3 == 0:
    return 'fuzz'
  elif num % 5 == 0:
    return 'buzz'
  return num
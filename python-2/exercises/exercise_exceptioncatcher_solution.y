error_types = []

"""
Handle each of these error-ful lines from the "Types of exceptions" slide with a try/catch for that specific kind of error.
Append each error to the error_types list.
"""

try:
  pow(2.12, 1000)
except OverflowError as e:
  error_types.append(type(e))

try:
  'hello'[1] = 'j'
except TypeError as e:
  error_types.append(type(e))

try:
  'hello'[7]
except IndexError as e:
  error_types.append(type(e))

try:
  x += 5
except NameError as e:
  error_types.append(type(e))

try:
  open('dsfdfd.txt')
except FileNotFoundError as e:
  error_types.append(type(e))


# At this point, error_types should store all the error types

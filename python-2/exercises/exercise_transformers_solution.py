def transform_list(old_list, transformer):
    """Returns a new list with each item transformed by transformer."""
    new_list = []
    for item in old_list:
        new_list.append(transformer(item))
    return new_list

def square(n):
  return n * n

def cube(n):
  return n * n * n

def bleep(text):
  return text.replace("dang", "***")


# Transform the list of numbers using the square function,
# and store result in the squared variable
numbers = [1, 2, 3]
squared = transform_list(numbers, square)

# Transform the list of numbers using the cube function,
# and store result in the cubed variable
numbers = [5, 6, 7]
cubed = transform_list(numbers, cube)

# Transform list of messages using the bleep function,
# and store result in the bleeped variable
messages = ["what the dang", "that dang nail", "dang it all"]
bleeped = transform_list(messages, bleep)


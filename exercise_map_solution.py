def square(n):
  return n * n

def cube(n):
  return n * n * n

def bleep(text):
  return text.replace("dang", "***")

# Map the list of numbers using the square function,
# and store result in the squared variable
numbers = [1, 2, 3]
squared = list(map(square, numbers))

# Map the list of numbers using the cube function,
# and store result in the cubed variable
numbers = [5, 6, 7]
cubed = list(map(cube, numbers))

# Map the list of messages using the bleep function,
# and store result in the bleeped variable
messages = ["what the dang", "that dang nail", "dang it all"]
bleeped = list(map(bleep, messages))

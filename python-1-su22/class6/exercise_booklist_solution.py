""""
Keep track of which books you read and which books you want to read!

Part 1:
Create a list of dictionaries, where each dictionary describes a book and has properties for:
* title (a string)
* author (a string)
* read (a boolean indicating if you read it yet).
"""

# Store the list of book dictionaries in this variable:
books = [
  {"title": "Uncanny Valley",
  "author": "Anna Wiener",
  "read": False
  },
  {"title": "Parable of the Sower",
  "author": "Octavia E. Butler",
  "read": True
  }
]

# Store the first book's title in this variable
# by referencing the books variable in some way:
first_title = books[0]["title"]

# Store the first book's author in this variable
# by referencing the books variable in some way:
first_author = books[0]["author"]

"""
Part 2:

Define this function so that it counts the number
of unread books in the list and returns the count.
"""
def count_unread_books(books):
  # Initialize a count to 0
  # Iterate through the books
  # If a book is not read, increment count
  # Return count
  count = 0
  for book in books:
    if not book["read"]:
      count += 1
  return count

# Note: The test will check this function with a
# different list of books.
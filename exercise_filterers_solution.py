def filter_list(old_list, filter):
    """Returns a new list with only items that pass the filter."""
    new_list = []
    for item in old_list:
        if filter(item):
            new_list.append(item)
    return new_list


def is_odd(num):
  return num % 2 == 1

def is_positive(num):
  return num > 0

def starts_with_f(text):
  return text[0].lower() == "f"


# Filter the list of numbers using the is_odd function,
# and store result in the odds variable
numbers = [37, 38, 39, 40, 41, 43]
odds = filter_list(numbers, is_odd)

# Filter the list of numbers using the is_positive function,
# and store result in the positives variable
numbers = [-23, 0, 13, -7, 22, 51]
positives = filter_list(numbers, is_positive)

# Filter list of words using the starts_with_f function,
# and store result in the fwords variable
words = ["lily", "fern", "frond", "daisy"]
fwords = filter_list(words, starts_with_f)


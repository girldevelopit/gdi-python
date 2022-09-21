"""
Complete the mix_up function. It should take in two strings, and return the concatenation of the two strings (separated by a space), slicing out and swapping the first 2 characters of each. You can assume that the strings are at least 2 characters long.
"""
def mix_up(word1, word2):
  """
  >>> mix_up('mix', 'pod')
  'pox mid'
  >>> mix_up('dog', 'dinner')
  'dig donner'
  """
  return word2[0:2] + word1[2:] + ' ' + word1[0:2] + word2[2:]

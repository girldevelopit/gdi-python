"""
Complete the not_bad function which takes a single string argument.
* It should find the first appearance of the substring 'not' and 'bad'.
* If the 'bad' follows the 'not', then it should replace the whole 'not'...'bad' substring with 'good' and return the result.
* If it doesn't find 'not' and 'bad' in the right sequence (or at all), just return the original sentence.
"""
def not_bad(sentence):
  """
  >>> not_bad('This dinner is not that bad!')
  'This dinner is good!'
  >>> not_bad('This movie is not so bad!')
  'This movie is good!'
  >>> not_bad('This dinner is bad!')
  'This dinner is bad!'
  """
  not_index = sentence.find('not')
  bad_index = sentence.find('bad')
  if not_index == -1 or bad_index == -1 or bad_index < not_index:
    return sentence
  return sentence[0:not_index] + 'good' + sentence[bad_index+3:]
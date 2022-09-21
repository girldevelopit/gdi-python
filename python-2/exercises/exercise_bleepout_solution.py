"""
Complete the bleep_out function. It should take two string arguments and return a version of the first string where all occurences of the second string have been replaced by '***'.
"""
def bleep_out(string1, string2):
  """
  >>> bleep_out('i freaking love carrots', 'freaking')
  'i *** love carrots'
  >>> bleep_out('oh dang oh dang oh dang', 'dang')
  'oh *** oh *** oh ***'
  """
  return string1.replace(string2, "***")
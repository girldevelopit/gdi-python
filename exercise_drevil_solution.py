"""
Complete the dr_evil function. It should take a single argument, an amount, and return '<amount> dollars', except it will add '(pinky)' at the end if the amount is 1 million or more."
"""
def dr_evil(amount):
  """
  >>> dr_evil(10)
  '10 dollars'
  >>> dr_evil(1000000)
  '1000000 dollars (pinky)'
  >>> dr_evil(2000000)
  '2000000 dollars (pinky)'
  """
  if amount >= 1000000:
    return f"{amount} dollars (pinky)"
  else:
    return f"{amount} dollars"
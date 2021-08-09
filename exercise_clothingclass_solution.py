"""
Clothing is a class that represents pieces of clothing in a closet. It tracks the color, category, and clean/dirty state.
"""
class Clothing:
  """
  >>> blue_shirt = Clothing("shirt", "blue")
  >>> blue_shirt.category
  'shirt'
  >>> blue_shirt.color
  'blue'
  >>> blue_shirt.is_clean
  True
  >>> blue_shirt.wear()
  >>> blue_shirt.is_clean
  False
  >>> blue_shirt.clean()
  >>> blue_shirt.is_clean
  True
  """

  # Write an __init__ method
  def __init__(self, category, color):
    self.category = category
    self.color = color
    self.is_clean = True

  # Write the wear() method
  def wear(self):
    self.is_clean = False

  # Write the clean() method
  def clean(self):
    self.is_clean = True
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

  def __init__(self, category, color):
    self.category = category
    self.color = color
    self.is_clean = True

  def wear(self):
    self.is_clean = False

  def clean(self):
    self.is_clean = True

class KidsClothing(Clothing):
  """
  >>> onesie = KidsClothing("onesie", "polka dots")
  >>> onesie.wear()
  >>> onesie.is_clean
  False
  >>> onesie.clean()
  >>> onesie.is_clean
  False
  >>> dress = KidsClothing("dress", "rainbow")
  >>> dress.clean()
  >>> dress.is_clean
  True
  >>> dress.wear()
  >>> dress.is_clean
  False
  >>> dress.clean()
  >>> dress.is_clean
  False
  """

  # Override the clean() method
  # so that kids clothing always stays dirty!
  def clean(self):
    self.is_clean = self.is_clean
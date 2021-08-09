"""
This class represents articles on an educational website.

Add a class variable for the license attribute,
which is always equal to "CC-BY-NC-SA".
"""
class Article:
  """
  >>> article1 = Article("Logic", "Samuel Tarín")
  >>> article1.get_byline()
  'By Samuel Tarín, License: CC-BY-NC-SA'
  >>> article2 = Article("Loops", "Pamela Fox")
  >>> article2.get_byline()
  'By Pamela Fox, License: CC-BY-NC-SA'
  """
  license = 'CC-BY-NC-SA'

  def __init__(self, title, author):
    self.title = title
    self.author = author

  def get_byline(self):
    return f"By {self.author}, License: {self.license}"
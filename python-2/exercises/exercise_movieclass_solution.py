"""
MoviePurchase is a class that represents movie purchases on YouTube. It tracks the title and cost of each movie bought, as well as the number of times the movie is watched.
"""
class MoviePurchase:
  """
  >>> ponyo = MoviePurchase("Ponyo", 19.99)
  >>> ponyo.title
  'Ponyo'
  >>> ponyo.cost
  19.99
  >>> ponyo.times_watched
  0
  >>> ponyo.watch()
  >>> ponyo.watch()
  >>> ponyo.times_watched
  2
  """

  def __init__(self, title, cost):
    # Fill out this function
    self.title = title
    self.cost = cost
    self.times_watched = 0

  def watch(self):
    # Fill out this function
    self.times_watched += 1

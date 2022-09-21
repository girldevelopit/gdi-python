class LearnableContent:
  """A base class for specific kinds of learnable content.
  All kinds have title and author attributes,
  but each kind may have additional attributes.
  """
  license = "Creative Commons"

  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    return f"{self.title} by {self.author}"

# Create a Video subclass with
# license of "YouTube Standard License"
class Video(LearnableContent):
  license = "YouTube Standard License"


# Create an Article subclass with
# license of "CC-BY-NC-SA"
class Article(LearnableContent):
  license = "CC-BY-NC-SA"


# In this variable, store a new Video instance with a title of "DNA" and an author of "Megan"
dna_video = Video("DNA", "Megan")


# In this variable, store a new Article instance with a title of "Water phases" and an author of "Lauren"
water_article = Article("Water phases", "Lauren")
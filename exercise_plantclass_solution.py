"""
This class is used by a plant nursery to track what plants they have in inventory and how many they have of each plant.
"""

class Plant:
  """
  >>> milkweed = Plant("Narrow-leaf milkweed", "Asclepias fascicularis")
  >>> milkweed.common_name
  'Narrow-leaf milkweed'
  >>> milkweed.latin_name
  'Asclepias fascicularis'
  >>> milkweed.inventory
  0
  >>> milkweed.update_inventory(2)
  >>> milkweed.inventory
  2
  """

  def __init__(self, common_name, latin_name):
    self.common_name = common_name
    # Fill out the rest of this function
    self.latin_name = latin_name
    self.inventory = 0

  def update_inventory(self, amount):
    # Fill out this function
    self.inventory += amount
    pass

"""
This class represents a character in a video game.
It tracks their name and health.
"""
class Character:
  """
  >>> player = Character("Mario")
  >>> player.name
  'Mario'
  >>> player.health
  100
  >>> player.damage(10)
  >>> player.health
  90
  >>> player.boost(5)
  >>> player.health
  95
  """
  def __init__(self, name):
    # Fill out this function
    self.name = name
    self.health = 100

  def damage(self, amount):
    # Fill out this function
    self.health -= amount

  def boost(self, amount):
    # Fill out this function
    self.health += amount

# Fill out the damage and boost methods per the comments.
class Boss(Character):
  """
  >>> mx_boss = Boss("Mx Boss Person")
  >>> mx_boss.damage(100)
  >>> mx_boss.health
  99
  >>> mx_boss.damage(10)
  >>> mx_boss.health
  98
  >>> mx_boss.boost(1)
  >>> mx_boss.health
  100
  """
  def damage(self, amount):
    # Bosses ignore the amount and instead always receive 1 unit of damage to their health
    self.health -= 1

  def boost(self, amount):
    # Bosses always receive twice the amount of boost to their health
    self.health += amount * 2


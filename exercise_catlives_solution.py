class Pet():
  def __init__(self, name, owner):
    self.is_alive = True
    self.name = name
    self.owner = owner

  def eat(self, thing):
    print(self.name + " ate a " + str(thing) + "!")

  def talk(self):
    print(self.name)

class Cat(Pet):
  """
  >>> angel = Cat("Angel", "Hunter")
  >>> angel.name
  'Angel'
  >>> angel.owner
  'Hunter'
  >>> angel.lives
  9
  >>> angel.is_alive
  True
  >>> angel.talk()
  Angel says meow!
  >>> angel.lose_life()
  >>> angel.lose_life()
  >>> angel.lose_life()
  >>> angel.lose_life()
  >>> angel.lose_life()
  >>> angel.lives
  4
  >>> angel.lose_life()
  >>> angel.lose_life()
  >>> angel.lose_life()
  >>> angel.lose_life()
  >>> angel.lives
  0
  >>> angel.is_alive
  False
  """
  def __init__(self, name, owner, lives=9):
    # Call super class to set name and owner
    # Set lives attribute
    super().__init__(name, owner)
    self.lives = lives
    pass

  def talk(self):
    # Print out '<name> says meow!'
    print(f'{self.name} says meow!')
    pass

  def lose_life(self):
    # Decrement a cat's life by 1
    # When lives reaches zero, set is_alive to False
    self.lives -= 1
    if self.lives <= 0:
      self.is_alive = False
    pass


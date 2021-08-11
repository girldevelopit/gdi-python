class Pet():
  def __init__(self, name, owner):
    self.is_alive = True
    self.name = name
    self.owner = owner

  def eat(self, thing):
    print(self.name + " ate a " + str(thing) + "!")

  def talk(self):
    print(self.name)

class Dog(Pet):
  """
  >>> cooper = Dog("Cooper", "Tinu")
  >>> cooper.name
  'Cooper'
  >>> cooper.owner
  'Tinu'
  >>> cooper.talk()
  Cooper says BARK!
  """

  def talk(self):
    print(f"{self.name} says BARK!")

# Fix this to inherit from Dog
class NoisyDog(Dog):
  """
  >>> roxy = NoisyDog("Roxy", "Joe")
  >>> roxy.name
  'Roxy'
  >>> roxy.owner
  'Joe'
  >>> roxy.talk()
  Roxy says BARK!
  Roxy says BARK!
  Roxy says BARK!
  """

  def talk(self):
    # Make it so that noisy dogs say the same thing,
    # but always say it three times!
    # Try to use super() to call the relevant superclass method
    super().talk()
    super().talk()
    super().talk()
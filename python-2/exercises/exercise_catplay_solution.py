class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += self.interact_increment
        print(f"Yay happy fun time with {animal2.name}")

class Cat(Animal):
  """
  >>> adult = Cat("Winston", 12)
  >>> adult.name
  'Winston'
  >>> adult.age
  12
  >>> adult.play_multiplier
  3
  >>> kitty = Cat("Kurty", 0.5)
  >>> kitty.name
  'Kurty'
  >>> kitty.age
  0.5
  >>> kitty.play_multiplier
  6
  """
  species_name = "Domestic cat"
  scientific_name = "Felis silvestris catus"
  calories_needed = 200
  play_multiplier = 3

  def __init__(self, name, age):
    #  Call the super class to set name and age
    # If age is less than 1, set play multiplier to 6
    super().__init__(name, age)
    if self.age < 1:
      self.play_multiplier = 6
    pass
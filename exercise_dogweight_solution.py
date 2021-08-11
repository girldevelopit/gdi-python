class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten = 0
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


class Dog(Animal):
  """
  >>> spot = Dog("Spot", 5, 20)
  >>> spot.name
  'Spot'
  >>> spot.age
  5
  >>> spot.weight
  20
  >>> spot.calories_needed
  400
  >>> puppy = Dog("Poppy", 1, 7)
  >>> puppy.name
  'Poppy'
  >>> puppy.age
  1
  >>> puppy.weight
  7
  >>> puppy.calories_needed
  140
  """
  species_name = "Domestic dog"
  scientific_name = "Canis lupus familiaris"
  calories_needed = 200

  def __init__(self, name, age, weight):
    #  Call the super class to set name and age
    #  Set the weight attribute
    #  Set calories_needed to 20x the weight
    super().__init__(name, age)
    self.weight = weight
    self.calories_needed = 20 * weight
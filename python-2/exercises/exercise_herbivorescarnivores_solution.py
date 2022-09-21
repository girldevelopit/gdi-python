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

class Herbivore(Animal):

    def eat(self, food):
        if food.type == "meat":
            self.happiness -= 5
        else:
            super().eat(food)

class Carnivore(Animal):

    def eat(self, food):
        if food.type == "meat":
            super().eat(food)

class Food():

  def __init__(self, name, type, calories):
    self.name = name
    self.type = type
    self.calories = calories

# Fix this class so it inherits from the correct subclass
class Zebra(Herbivore):
  """
  >>> zebby = Zebra("Zebby", 12)
  >>> zebby.play(2)
  WHEEE PLAY TIME!
  >>> zebby.happiness
  4
  >>> zebby.eat(Food("Broccoli", "vegetable", 100))
  Om nom nom yummy Broccoli
  >>> zebby.calories_eaten
  100
  >>> zebby.eat(Food("Beef", "meat", 300))
  >>> zebby.happiness
  -1
  >>> zebby.calories_eaten
  100
  """
  species_name = "Common Zebra"
  scientific_name = "Equus quagga"
  calories_needed = 15000


# Fix this class so it inherits from the correct subclass
class Hyena(Carnivore):
  """
  >>> helen = Hyena("Helen", 12)
  >>> helen.play(2)
  WHEEE PLAY TIME!
  >>> helen.happiness
  4
  >>> helen.eat(Food("Carrion", "meat", 300))
  Om nom nom yummy Carrion
  >>> helen.calories_eaten
  300
  >>> helen.happiness
  4
  >>> helen.eat(Food("Broccoli", "vegetable", 100))
  >>> helen.calories_eaten
  300
  >>> helen.happiness
  4
  """
  species_name = "Striped Hyena"
  scientific_name = "Hyaena hyaena"
  calories_needed = 1000
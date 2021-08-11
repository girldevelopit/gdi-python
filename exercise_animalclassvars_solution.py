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


# Create a Sloth class with
# species_name "Hoffmann's two-toed sloth"
# scientific_name "Choloepus hoffmanni"
# calories_needed 680
class Sloth(Animal):
  species_name = "Hoffmann's two-toed sloth"
  scientific_name = "Choloepus hoffmanni"
  calories_needed = 680

# Create a Cat class with
# species_name "Domestic cat"
# scientific_name "Felis silvestris catus"
# calories_needed 200
# play_multiplier 3
# interact_increment 0
class Cat(Animal):
  species_name = "Domestic cat"
  scientific_name = "Felis silvestris catus"
  calories_needed = 200
  play_multiplier = 3
  interact_increment = 0


# In this variable, store a Sloth instance with a name of "Buttercup" and an age of 27
buttercup = Sloth("Buttercup", 27)

# In this variable, store a Cat instance with a name of "Jackson" and an age of 8
jackson = Cat("Jackson", 8)


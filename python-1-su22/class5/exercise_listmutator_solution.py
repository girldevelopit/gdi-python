## CITIES
cities = ['London', 'Constantinople', 'Sydney', 'Leningrad', 'Peking']

# Use bracket notation to change:
# Constantinople to Istanbul
# Leningrad to Saint Petersburg
# Peking to Beijing
cities[1] = 'Istanbul'
cities[3] = 'Saint Petersburg'
cities[4] = 'Beijing'


## DINOSAURS
dinos = ['Tyrannosaurus rex', 'Torosaurus', 'Stegosaurus', 'Brontosaurus']

# Use bracket notation to change:
# Torosaurus to Triceratops
# Brontosaurus to Apatosaurus
dinos[1] = 'Triceratops'
dinos[3] = 'Apatosaurus'


## PLANETS
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

# Remove the last planet using a list method
# and store it in this variable:
not_actually_a_planet = planets.pop()


## GYMNASTS
team_usa = ['Simone Biles']
original_length = len(team_usa)

# Use a list method to add more gymnasts to the list:
# Sunisa Lee, Jordan Chiles, Grace McCallum, MyKayla Skinner
team_usa.append("Sunisa Lee")
team_usa.append("Jordan Chiles")
team_usa.append("Grace McCallum")
team_usa.append("MyKayla Skinner")

# When you're done, there should be 5 gymnasts in the list
new_length = len(team_usa)
""" This function should return a string like
"There are NUM planets in the solar system"
where NUM is provided as an argument."""
def solar_system(num_planets):
  # Replace this line!
  return f"There are {num_planets} planets in the solar system"

# Should equal "There are 8 planets in the solar system"
ss1 = solar_system(8)

# Should equal "There are 9 planets in the solar system"
ss2 = solar_system(9)

""" This function should return a string of the format
"On the DAYth day of MONTH in the year YEAR"
where DAY, MONTH, and YEAR are provided.
"""
def fancy_date(month, day, year):
  # Replace this line!
  return f"On the {day}th day of {month} in the year {year}"

# Should equal "On the 8th day of July in the year 2019"
date1 = fancy_date("July", 8, 2019)
# Should equal "On the 24th day of June in the year 1984"
date2 = fancy_date("June", 24, 1984)


""" This function should return a string
which starts with the provided place, then
has an @ sign, then the comma-separated lat and lng"""
def location(place, lat, lng):
  # Replace this line!
  return f"{place} @ {lat}, {lng}"

# Should equal "Tilden Farm @ 37.91, -122.29"
loc1 = location("Tilden Farm", 37.91, -122.29)
# Should equal "Salton Sea @ 33.309, -115.979"
loc2 = location("Salton Sea", 33.309,-115.979)


""" This function should return a string
which starts with the provided item,
then a colon, then a $ sign and the provided cost."""
def menu(item, cost):
  return f"{item}: ${cost}"

# Should equal "Avocado toast: $9.99"
menu1 = menu("Avocado toast", 9.99)
# Should equal "Cronut: $3.99"
menu2 = menu("Cronut", 3.99)
def solar_system(num_planets):
  return "There are " + str(num_planets) + " planets in the solar system"

def menu(item, cost):
  return item + ": $" + str(cost)

def location(place, lat, lng):
  return place + " @ " + str(lat) + ", " + str(lng)

def fancy_date(month, day, year):
  return "On the " + str(day) + "th day of " + month + " in the year " + str(year)
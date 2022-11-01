"""
How can we communicate the highs and lows of climate change with people who use a different temperature unit?
Let's make a temperature converter based on the steps here:
https://www.mathsisfun.com/temperature-conversion.html

Create a function called celsius_to_fahrenheit that:
* takes a single argument, the temperature in celsius
* calculates and returns the fahrenheit equivalent

Similarly, create another function called fahrenheit_to_celsius that:
* takes a single argument, the temperature in fahrenheit
* calculates and returns the celsius equivalent
"""

def celsius_to_fahrenheit(celsius):
  # Divide by 5, then multiply by 9, then add 32
  return ((celsius / 5) * 9) + 32

def fahrenheit_to_celsius(fahrenheit):
  # Deduct 32, then multiply by 5, then divide by 9
  return ((fahrenheit - 32) * 5) / 9

# Test 1: 0 degrees celsius should return 32 fahrenheight
f1 = celsius_to_fahrenheit(0)
print(f1)

# Test 2: 100 degrees celsius should return 212
f2 = celsius_to_fahrenheit(100)
print(f2)

# Test 3:  32 degrees fahrenheit should return 0 celsius
c1 = fahrenheit_to_celsius(32)
print(c1)

# Test 4: 212 degrees celsius should return 100 celsius
c2 = fahrenheit_to_celsius(212)
print(c2)

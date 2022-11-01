"""
Ever wonder how much a "lifetime supply" of your favorite snack is? Wonder no more!

Write a function named calculate_supply that:
* takes 2 arguments: age, amount per day.
* calculates the amount consumed for rest of the life (based on a constant max age of 81).
* returns the result
"""

# Write the def statement here!
def calculate_supply(age, amount_per_day):
  years_remaining = 81 - age
  lifetime_amount = years_remaining * (amount_per_day * 365)
  return round(lifetime_amount)

# Test 1: Should return 365
amount1 = calculate_supply(80, 1)
print(amount1)

# Test 2: Should return 730
amount2 = calculate_supply(80, 2)
print(amount2)

# Test 3: Should return 49275
amount3 = calculate_supply(36, 3)
print(amount3)

# Bonus: Accept floating point values for amount per day, and round the result up to an integer.

# Bonus Test 4: Should return 34850
amount4 = calculate_supply(37, 2.17)
print(amount4)

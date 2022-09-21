"""
You know how old a dog is in human years, but what about dog years? Calculate it!

Write a function named calculate_dog_age that:
* takes 1 argument: a dog's age in human years.
* calculates the dog's age based on the conversion rate of 1 human year to 7 dog years.
* returns the age in dog years.
"""

# Write the def statement here!
def calculate_dog_age(human_years):
    return human_years * 7

# Test 1: Should return 7
age1 = calculate_dog_age(1)

# Test 2: Should return 3.5
age2 = calculate_dog_age(0.5)

# Test 3: Should return 84
age3 = calculate_dog_age(12)
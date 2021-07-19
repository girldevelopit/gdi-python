# Make a range from 0-5
range1 = ''
for num in range(6):
  range1 += str(num) + '.'
# range1 should store 0.1.2.3.4.5.

# Make a range from 0-9
range2 = ''
for num in range(10):
  range2 += str(num) + '.'
# range1 should store 0.1.2.3.4.5.6.7.8.9.

# Make a range from 10-15
range3 = ''
for num in range(10, 16):
  range3 += str(num) + '.'
# range2 should store 10.11.12.13.14.15.

# Make a range of every third number from 3-15
range4 = ''
for num in range(3, 16, 3):
  range4 += str(num) + '.'
# range3 should store 3.6.9.12.15.
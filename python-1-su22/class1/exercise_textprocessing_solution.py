# In the console, past the following lines and press Enter:

import string

# In the console, type the string method that transforms text as described below.
# Press Enter after typing each method to check your work

# Some common string methods are:
# .upper()
# .lower()
# .title()
# .swapcase()
# .strip()
# See https://www.w3schools.com/python/python_ref_string.asp for more!

# NOTE! Methods are formatted differently from from function calls - the string goes before the method instead of inside the (). You can either assign a name to the string, like str = 'blar' and then str.upper() or use enter the string directly, like 'blar'.upper()

# Q1: Turn 'STOP YELLING!'
# into 'stop yelling!'
str = 'STOP YELLING!'
str.lower()

# Q2: Turn 'hey, wait for me!'
# into 'HEY, WAIT FOR ME!'
str = 'hey, wait for me!'
str.upper()

# Q3: Turn 'a tale of two cities'
# into 'A Tale Of Two Cities'
str = 'a tale of two cities'
str.title()

# Q4: Turn 'oOooOOoooOOO'
# into 'OoOOooOOOooo'
str = 'oOooOOoooOOO'
str.swapcase()

## Chained methods!
# Q5: Turn '  banana  '
# into 'BANANA'
str = '  banana  '
str.strip().upper()
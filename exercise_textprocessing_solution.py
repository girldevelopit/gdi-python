from texter import uppercase, lowercase, binarize, clapify, emojify, exclamify, mystery

# Use the imported functions to turn the string into the expected text. Try in console and run the tests to check your work.

# Q: Turn this text into 'STOP YELLING!'
q1 = 'stop yelling!'
a1 = uppercase(q1)

# Q2: Turn this text into 'JğUğSğTğ ğDğOğ ğIğT'
q2 = 'JUST DO IT'
a2 = clapify(q2)

# Q3: Turn this text into 'This ğ is on ğ¥ !'
q3 = 'This world is on fire!'
a3 = emojify(q3)

# Q4: Turn this text into 'stp rdng my nts, dd!'
q4 = 'stop reading my notes, dad!'
a4 = mystery(q4)

## Nested expressions!
# Q5: Turn this text into 'IM SO ğ· OF ğ'
q5 = 'im so sick of cake'
a5 = uppercase(emojify(q5))

# Q6: Turn this text into 'sndng my â¤ï¸ !'
q6 = 'sending my love!'
a6 = mystery(emojify(q6))

# Q7: Turn this text into '01000001 01000010 01000011'
q7 = 'ABC'
a7 = binarize(uppercase(q7))

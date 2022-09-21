""" Fix the summation function so that the doctests work."""

def double(n):
  return n * 2

def square(n):
  return n * n

def cube(n):
  return n ** 3

def summation(n, term):
 """Sum the first n terms of a sequence.

 >>> summation(5, double)
 30
 >>> summation(5, square)
 55
 >>> summation(5, cube)
 225
 """
 total = 0
 k = 1
 while k <= n:
    total = total + term(k) # <-- FIX THIS LINE!
    k += 1
 return total


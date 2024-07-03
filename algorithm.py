#WHAT I LEARNED FROM THIS ACTIVITY IS IN THE README FILE theAlgorithm.md.
#Code converted from Javascript to Python3
import math
import unittest
class testValidity(unittest.TestCase):
  def test_equal(self):
    self.assertEqual(doSearch(primes, 113), 4)
    self.assertEqual(doSearch(primes, 137), 7)
    self.assertEqual(doSearch(primes, 191), 17)
      
def doSearch(array, targetValue):
  min = 0
  max = (len(array) - 1)
  guessNum = 0
  while max >= min:
    guess = math.floor((max+min)/2)
    guessNum += 1
    print(str(guess))
    if array[guess] == targetValue:
      print(str(guessNum))
      return guess
    elif array[guess] < targetValue:
      min = guess + 1
    else:
      max = guess - 1
  return -1
  
#Part of original Javascript code
#Data set used: List of all prime numbers from 101 to 200
primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
result = doSearch(primes, 113)
print("Found prime at index " + str(result))
result2 = doSearch(primes, 137)
print("Found prime at index " + str(result2))
result3 = doSearch(primes, 191)
print("Found prime at index " + str(result3))
unittest.main()

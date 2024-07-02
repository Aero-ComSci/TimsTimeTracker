#Code converted from Javascript to Python3
import math
import unittest
class testValidity(unittest.TestCase):
  def test_equal(self):
    self.assertEqual(doSearch(primes, 73), 20)
    self.assertEqual(doSearch(primes, 67), 18)
    self.assertEqual(doSearch(primes, 23), 8)
      
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
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
result = doSearch(primes, 73)
print("Found prime at index " + result)
result2 = doSearch(primes, 67)
print("Found prime at index " + result2)
result3 = doSearch(primes, 23)
print("Found prime at index " + result3)
unittest.main()

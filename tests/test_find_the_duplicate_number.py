from random import Random
from src.find_the_duplicate_number.solution import Solution

class TestFindTheDuplicateNumber:
  def test_sample_1(self):
    assert Solution().findDuplicate([1,3,4,2,2]) == 2
  
  def test_sample_2(self):
    assert Solution().findDuplicate([3,1,3,4,2]) == 3

  def test_randomized(self):
    rand = Random()
    length = rand.randint(1, 100)
    repeated = rand.randint(1, length - 1)

    arr = [i + 1 for i in range(length)] + [repeated]

    assert Solution().findDuplicate(arr) == repeated
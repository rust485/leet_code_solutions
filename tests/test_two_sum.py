from core.testing.list import lists_equal_unordered
from src.two_sum.solution import Solution

class TestTwoSum:
	def test_example_1(self):
		indices = Solution().twoSum([2, 7, 11, 15], 9)
		assert lists_equal_unordered(indices, [0, 1])

	def test_example_2(self):
		indices = Solution().twoSum([3, 2, 4], 6)
		assert lists_equal_unordered(indices, [1, 2])

	def test_example_3(self):
		indices = Solution().twoSum([3, 3], 6)
		assert lists_equal_unordered(indices, [0, 1])

	def test_example_4(self):
		indices = Solution().twoSum([3], 6)
		assert lists_equal_unordered(indices, [])
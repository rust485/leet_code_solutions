from src.maximum_subarray.solution import Solution

class TestMaximumSubarray:

	def test_example_1(self):
		assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

	def test_example_2(self):
		assert Solution().maxSubArray([1]) == 1

	def test_example_3(self):
		assert Solution().maxSubArray([5,4,-1,7,8]) == 23
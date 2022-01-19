from src.majority_element.solution import Solution

class TestMajorityElement:
	def test_example_1(self):
		assert Solution().majorityElement([3, 2, 3]) == 3

	def test_example_2(self):
		assert Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

	def test_example_3(self):
		assert Solution().majorityElement([2, 2]) == 2
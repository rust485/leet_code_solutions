from src.peak_index_in_mountain_array.solution import Solution

class TestPeakIndexInMountainArray:

	def test_example_1(self):
		assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1

	def test_example_2(self):
		assert Solution().peakIndexInMountainArray([0, 2, 1, 0]) == 1

	def test_example_3(self):
		assert Solution().peakIndexInMountainArray([0, 10, 5, 2]) == 1
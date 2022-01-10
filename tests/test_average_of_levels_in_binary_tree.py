from typing import List
from core.testing.tree import build_tree
from src.average_of_levels_in_binary_tree.solution import Solution

def get_avgs(l: List[int]) -> List[int]:
	return Solution().averageOfLevels(build_tree(l))


class TestAverageOfLevelsInBinaryTree:

	def test_example_1(self):
		assert get_avgs([3, 9, 20, None, None, 15, 7]) == [3, 14.5, 11]

	def test_example_2(self):
		assert get_avgs([3, 9, 20, 15, 7]) == [3, 14.5, 11]

	def test_full_tree(self):
		assert get_avgs([3, 9, 20, 15, 3, 15, 7]) == [3, 14.5, 10]
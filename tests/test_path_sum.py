from typing import List
from core.testing.tree import build_compact_tree, build_tree

from src.path_sum.solution import Solution

def path_sum(l: List[int], target: int) -> bool:
	return Solution().hasPathSum(build_tree(l), target)

class TestPathSum:
	
	def test_example_1(self):
		assert path_sum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1], 22)

	def test_example_2(self):
		assert not path_sum([1, 2, 3], 5)

	def test_example_3(self):
		assert not path_sum([], 0)
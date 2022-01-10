from typing import List
from core.testing.tree import build_tree
from src.same_tree.solution import Solution

def are_same(l1: List[int], l2: List[int]) -> bool:
	return Solution().isSameTree(build_tree(l1), build_tree(l2))

class TestSameTree:
	def test_same_tree(self):
		assert are_same([1, 2, 3], [1, 2, 3])

	def test_flipped_tree(self):
		assert not are_same([1, 2], [1, None, 2])

	def test_same_tree_structure_but_diff_values(self):
		assert not are_same([1, 2, 1], [1, 1, 2])
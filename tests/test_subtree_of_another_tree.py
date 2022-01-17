from typing import Any, List
from core.testing.tree import build_compact_tree
from src.subtree_of_another_tree.solution import Solution

def is_subtree(root: List[Any], subroot: List[Any]) -> bool:
	r,s = build_compact_tree(root), build_compact_tree(subroot)
	return Solution().isSubtree(r, s)

class TestSubtreeOfAnotherTree:
	def test_example_1(self):
		assert is_subtree([3, 4, 5, 1, 2], [4, 1, 2])

	def test_example_2(self):
		assert not is_subtree([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2])

	def test_trees_are_equal(self):
		assert is_subtree([3, 4], [3, 4])

	def test_sample(self):
		assert not is_subtree([3, 4, 5, 1, None, 2], [3,1,2])

	def test_subtree_with_one_node(self):
		assert not is_subtree([3, 4, 5], [3])
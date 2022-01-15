from typing import Any, List
from core.testing.tree import build_compact_tree

from src.diameter_of_binary_tree.solution import Solution


def get_diameter(l: List[Any]) -> int:
	return Solution().diameterOfBinaryTree(build_compact_tree(l))

class TestDiameterOfBinaryTree:
	def test_tree_with_only_1_node(self):
		assert get_diameter([1]) == 0

	def test_example_1(self):
		assert get_diameter([1, 2, 3, 4, 5]) == 3

	def test_example_2(self):
		assert get_diameter([1, 2]) == 1

	def test_basic_tree(self):
		assert get_diameter([1, 2, 3, 4, None, None, 5]) == 4

	def test_tree_with_only_left_nodes(self):
		assert get_diameter([1, 2, None, 3, None, 4, None, 5, None, 6]) == 5

	def test_tree_where_root_not_in_longest_path(self):
		assert get_diameter([1, 2, None, 3, 4, None, 5, 6, None, 7]) == 5
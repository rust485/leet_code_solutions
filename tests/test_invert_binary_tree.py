from typing import Any, List, Optional
from core.testing.tree import build_compact_tree, trees_are_equivalent
from core.model.treenode import TreeNode
from src.invert_binary_tree.solution import Solution

def invert_tree(l: List[Any]) -> Optional[TreeNode]:
	return Solution().invertTree(build_compact_tree(l))

class TestInvertBinaryTree:
	def test_example_1(self):
		inverted = invert_tree([4, 2, 7, 1, 3, 6, 9])
		expected = build_compact_tree([4, 7, 2, 9, 6, 3, 1])
		assert trees_are_equivalent(inverted, expected)

	def test_example_2(self):
		inverted = invert_tree([2, 1, 3])
		expected = build_compact_tree([2, 3, 1])
		assert trees_are_equivalent(inverted, expected)

	def test_example_3(self):
		inverted = invert_tree([])
		assert trees_are_equivalent(inverted, None)

	def test_uneven_tree(self):
		inverted = invert_tree([1, 2])
		expected = build_compact_tree([1, None, 2])
		assert trees_are_equivalent(inverted, expected)
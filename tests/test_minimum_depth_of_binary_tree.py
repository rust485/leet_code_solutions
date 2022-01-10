from typing import Any, List
from core.model.treenode import TreeNode
from core.testing.tree import build_tree
from src.minimum_depth_of_binary_tree.solution import Solution

def get_min_depth(l: List[Any]) -> int:
	return Solution().minDepth(build_tree(l))

class TestMinimumDepthOfBinaryTree:

	def test_empty_tree(self):
		assert get_min_depth([]) == 0

	def test_tree_with_only_head(self):
		assert get_min_depth([5]) == 1

	def test_example_1(self):
		assert get_min_depth([3, 9, 20, None, None, 15, 7]) == 2

	def test_example_2(self):
		h = TreeNode(2)
		h.right = TreeNode(3)
		h.right.right = TreeNode(4)
		h.right.right.right = TreeNode(5)
		h.right.right.right.right = TreeNode(6)
		assert Solution().minDepth(h) == 5
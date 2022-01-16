from core.testing.tree import build_compact_tree
from src.maximum_depth_of_binary_tree.solution import Solution

class TestMaximumDepthOfBinaryTree:
	def test_empty_tree(self):
		assert Solution().maxDepth(None) == 0

	def test_tree_with_only_root(self):
		assert Solution().maxDepth(build_compact_tree([5])) == 1

	def test_example_1(self):
		assert Solution().maxDepth(build_compact_tree([3, 9, 20, None, None, 15, 7])) == 3

	def test_example_2(self):
		assert Solution().maxDepth(build_compact_tree([1, None, 2])) == 2
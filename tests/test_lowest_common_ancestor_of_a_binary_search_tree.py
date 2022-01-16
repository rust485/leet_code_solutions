from typing import Any, List
from core.model.treenode import TreeNode
from core.testing.tree import build_compact_tree
from src.lowest_common_ancestor_of_a_binary_search_tree.solution import Solution


class TestLowestCommonAncestorOfABinarySearchTree:
	def test_example_1(self):
		root = build_compact_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
		p = root.left
		q = root.right

		assert Solution().lowestCommonAncestor(root, p, q) == root

	def test_example_2(self):
		root = build_compact_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
		p = root.left
		q = p.right

		assert Solution().lowestCommonAncestor(root, p, q) == p

	def test_example_3(self):
		root = build_compact_tree([2, 1])
		p = root
		q = root.left

		assert Solution().lowestCommonAncestor(root, p, q) == root

	def test_p_is_q(self):
		root = build_compact_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
		p = root.right.right
		q = p

		assert Solution().lowestCommonAncestor(root, p, q) == p

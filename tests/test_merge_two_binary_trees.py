from typing import List
from core.model.treenode import TreeNode
from core.testing.tree import build_compact_tree, trees_are_equivalent
from src.merge_two_binary_trees.solution import Solution

def merge_trees(l1: List[int], l2: List[int]) -> TreeNode:
	r1 = build_compact_tree(l1)
	r2 = build_compact_tree(l2)

	return Solution().mergeTrees(r1, r2)

class TestMergeTwoBinaryTrees:
	def test_empty_trees(self):
		merged = merge_trees([], [])
		assert merged is None

	def test_one_empty_tree(self):
		l1 = [5, 3, 7, None, 6, 1, None, 8]
		merged = merge_trees(l1, [])
		expected = build_compact_tree(l1)
		assert trees_are_equivalent(merged, expected)

	def test_two_trees_with_same_structure(self):
		merged = merge_trees([5, 3, 7, None, 6, 1, None, 8], [7, 21, 2, None, 4, 10, None, 3])
		expected = build_compact_tree([12, 24, 9, None, 10, 11, None, 11])
		assert trees_are_equivalent(merged, expected)

	def test_example_1(self):
		merged = merge_trees([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7])
		expected = build_compact_tree([3, 4, 5, 5, 4, None, 7])
		assert trees_are_equivalent(merged, expected)

	def test_example_2(self):
		merged = merge_trees([1], [1, 2])
		expected = build_compact_tree([2, 2])
		assert trees_are_equivalent(merged, expected)
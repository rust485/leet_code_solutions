from typing import Optional
from core.model.treenode import TreeNode

class Solution:
	def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
		if self.are_equal(root, subRoot):
			return True

		if not root:
			return False
		
		return self.isSubtree(root.left, subRoot) or \
			self.isSubtree(root.right, subRoot)

	def are_equal(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
		if not r1 and not r2:
			return True

		return r1 and r2 and r1.val == r2.val and \
			self.are_equal(r1.left, r2.left) and \
			self.are_equal(r1.right, r2.right)

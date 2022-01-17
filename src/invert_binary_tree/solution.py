from typing import Optional
from core.model.treenode import TreeNode

class Solution:
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		if root is None:
			return
				
		tmp = root.right
		root.right = root.left
		root.left = tmp

		self.invertTree(root.left)
		self.invertTree(root.right)

		return root
from typing import List, Optional
from core.model.treenode import TreeNode

class Solution:
	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		cur = root
		while cur is not None:
			if p.val < cur.val < q.val or q.val < cur.val < p.val \
				or cur.val == p.val or cur.val == q.val:
				break
			
			if p.val > cur.val:
				cur = cur.right
			else:
				cur = cur.left

		return cur
from typing import Optional

from core.model.treenode import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        
        return self.check_path(root, 0, target)
    
    def check_path(self, node: Optional[TreeNode], cur: int, target: int) -> bool:
        cur += node.val
        
        if not node.right and not node.left:
            return target == cur

        return \
			node.left and self.check_path(node.left, cur, target) or \
			node.right and self.check_path(node.right, cur, target)

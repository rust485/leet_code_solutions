from typing import Optional
from core.model.treenode import TreeNode

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.min_height(root) if root else 0
    
    def min_height(self, node: TreeNode) -> int:
        if not node.left and not node.right:
            return 1
        
        if node.right and node.left:
            return min(self.min_height(node.right), self.min_height(node.left)) + 1
        elif node.right:
            return self.min_height(node.right) + 1
        
        return self.min_height(node.left) + 1
            
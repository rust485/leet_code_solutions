from typing import Optional
from core.model.treenode import TreeNode

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self._max = 0

        self._find_max_subtree(root)

        return self._max

    def _find_max_subtree(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        h_left = self._find_max_subtree(node.left)
        h_right = self._find_max_subtree(node.right)

        height = max(h_left, h_right) + 1

        dist = h_left + h_right
        self._max = max(dist, self._max)

        return height

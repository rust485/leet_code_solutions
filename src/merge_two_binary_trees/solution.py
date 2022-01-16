from typing import Optional
from core.model.treenode import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        merged_root = self._merge_two_nodes(root1, root2)

        self.merge_trees_rec(root1, root2, merged_root)

        return merged_root

    def merge_trees_rec(self, root1: Optional[TreeNode], root2: Optional[TreeNode], parent: Optional[TreeNode]):
        if not root1 and not root2:
            return

        l1, r1 = (root1.left, root1.right) if root1 else (None, None)
        l2, r2 = (root2.left, root2.right) if root2 else (None, None)

        parent.left = self._merge_two_nodes(l1, l2)
        parent.right = self._merge_two_nodes(r1, r2)

        self.merge_trees_rec(l1, l2, parent.left)
        self.merge_trees_rec(r1, r2, parent.right)

    def _merge_two_nodes(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not n1 and not n2: 
            return None
        
        v1 = n1.val if n1 else 0
        v2 = n2.val if n2 else 0

        return TreeNode(v1 + v2)

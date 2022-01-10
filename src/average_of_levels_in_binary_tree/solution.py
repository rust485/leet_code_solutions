from typing import List, Optional

from core.model.treenode import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        
        avgs = []
        
        while len(queue) != 0:
            _q = []
            
            total = 0
            for n in queue:
                total += n.val
                if n.right:
                    _q += [n.right]
                if n.left:
                    _q += [n.left]
                    
            avgs += [total/len(queue)]
            
            queue = _q
            
        return avgs
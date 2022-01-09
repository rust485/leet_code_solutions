from typing import Optional
from core.model.listnode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        
        cur = head
        while cur is not None:
            if cur in visited:
                return True
            
            visited.add(cur)
            cur = cur.next
        
        return False
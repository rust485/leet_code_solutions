from typing import Optional
from core.model.listnode import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        mid = head
        cur = head
        while cur is not None:
            if not i % 2:
                mid = mid.next
            cur = cur.next
            i += 1
            
        return mid
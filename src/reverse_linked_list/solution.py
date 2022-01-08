from typing import Optional
from core.model.listnode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        cur = head

        # this is an inplace reversal, we could instead use
        # a dummy head node and perform a recursive attachment to the dummy head node
        while cur is not None:
            # store the next node since we are about to overwrite the reference
            n = cur.next

            # point cur's next reference to its predecessor
            cur.next = prev

            prev = cur
            cur = n

        return prev

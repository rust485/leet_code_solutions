from typing import Optional
from core.model.listnode import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur = head.next
        prev = head

        # iterate through the list, to preserve the head node we remove the duplicates following the original value
        # if we find a duplicate, point the previous node to the duplicates next node and clear the duplicates next reference
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
                cur.next = None
                cur = prev.next
            else:
                prev = cur
                cur = cur.next

        return head

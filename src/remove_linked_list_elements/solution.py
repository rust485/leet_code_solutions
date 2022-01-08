from typing import Optional
from core.model.listnode import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        cur, prev = head, None
        while cur:
            if cur.val == val:
                if prev:
                    # point the previous node to the node immediately following removed node
                    prev.next = cur.next
                else:
                    # no previous node - we are removing the head node so we need to repoint head to the 2nd node
                    head = cur.next

                l = cur
                cur = cur.next
                l.next = None
            else:
                prev = cur
                cur = cur.next

        return head

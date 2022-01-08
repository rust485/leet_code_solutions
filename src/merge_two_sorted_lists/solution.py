from typing import Optional
from core.model.listnode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        c1 = list1
        c2 = list2

        head = None

        # initialize head and increment the appropriate pointer
        if not c1 or c2 and c1.val > c2.val:
            # if c1 is null or if c2 comes before c1
            head = ListNode(c2.val)
            c2 = c2.next
        else:
            # if c2 is null or c1 comes before c2
            head = ListNode(c1.val)
            c1 = c1.next

        cur = head
        while c1 or c2:
            # use the same logic from above, but now we are altering our moving pointer,
            # cur, which is originally set to head
            if not c1 or c2 and c1.val > c2.val:
                cur.next = ListNode(c2.val)
                c2 = c2.next
            else:
                cur.next = ListNode(c1.val)
                c1 = c1.next

            cur = cur.next

        return head

from core.model.listnode import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        first_half = []

        cur, mid = head, head

        i = 0
        while cur is not None:
            cur = cur.next
            if not i % 2 and cur:
                first_half += [mid.val]
                mid = mid.next
            i += 1

        cur = mid if not i % 2 else mid.next

        i = len(first_half) - 1
        while cur is not None and i >= 0:
            if cur.val != first_half[i]:
                return False

            i -= 1
            cur = cur.next

        return True

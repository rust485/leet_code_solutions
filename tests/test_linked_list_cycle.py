from core.model.listnode import ListNode
from src.linked_list_cycle.solution import Solution

class TestLinkedListCycle:

	def test_single_element(self):
		h = ListNode(5)

		assert not Solution().hasCycle(h) 

	def test_list_with_repeated_value_but_no_cycle(self):
		h = ListNode(5)
		h.next = ListNode(5)

		assert not Solution().hasCycle(h)

	def test_list_with_cycle_containing_head(self):
		h = ListNode(5)
		h.next = ListNode(7)
		h.next.next = h

		assert Solution().hasCycle(h)

	def test_list_with_cycle(self):
		h = ListNode(5)
		h.next = ListNode(7)
		h.next.next = ListNode(4)
		h.next.next.next = h.next

		assert Solution().hasCycle(h)

	def test_list_with_self_reference(self):
		h = ListNode(5)
		h.next = h

		assert Solution().hasCycle(h)
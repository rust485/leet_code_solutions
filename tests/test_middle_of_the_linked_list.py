from typing import List
from core.model.listnode import ListNode
from src.middle_of_the_linked_list.solution import Solution

class TestMiddleOfTheLinkedList:

	def test_list_len_1(self):
		h = ListNode(5)
		
		assert Solution().middleNode(h) == h

	def test_empty_list(self):
		assert Solution().middleNode(None) is None

	def test_odd_len_list(self):
		h = ListNode(5)
		h.next = ListNode(3)
		h.next.next = ListNode(7)

		assert Solution().middleNode(h) is h.next

	def test_even_len_list(self):
		h = ListNode(5)
		h.next = ListNode(3)
		h.next.next = ListNode(7)
		h.next.next.next = ListNode(8)

		assert Solution().middleNode(h) == h.next.next
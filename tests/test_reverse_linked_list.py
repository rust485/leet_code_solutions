from typing import Any, List, Optional

from core.testing.linked_list import assert_ll_equals_list, build_linked_list
from core.model.listnode import ListNode
from src.reverse_linked_list.solution import Solution


def reverse(l: List[Any]) -> Optional[ListNode]:
    return Solution().reverseList(build_linked_list(l))


class TestReverseLinkedList:

    def test_empty_list(self):
        h = reverse([])

        assert h is None

    def test_list_len_1(self):
        h = reverse([4])

        assert_ll_equals_list(h, [4])

    def test_list_with_multiple_elements(self):
        h = reverse([4, 10, 5, 7, 8, 12])

        assert_ll_equals_list(h, [12, 8, 7, 5, 10, 4])

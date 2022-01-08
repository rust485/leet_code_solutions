from typing import Any, List, Optional

from core.testing.linked_list import assert_ll_equals_list, build_linked_list
from core.model.listnode import ListNode
from src.remove_linked_list_elements.solution import Solution


def remove_elements(l: List[Any], target: int) -> Optional[ListNode]:
    return Solution().removeElements(build_linked_list(l), target)


class TestRemoveLinkedListElements:
    def test_empty_list(self):
        h = remove_elements([], 10)

        assert_ll_equals_list(h, [])

    def test_target_not_in_list(self):
        h = remove_elements([1, 2, 3, 4], 5)

        assert_ll_equals_list(h, [1, 2, 3, 4])

    def test_target_is_only_element(self):
        h = remove_elements([1], 1)

        assert_ll_equals_list(h, [])

    def test_target_is_head(self):
        h = remove_elements([1, 2, 3, 4, 5], 1)

        assert_ll_equals_list(h, [2, 3, 4, 5])

    def test_target_is_tail(self):
        h = remove_elements([1, 2, 3, 4, 5], 5)

        assert_ll_equals_list(h, [1, 2, 3, 4])

    def test_target_is_head_and_tail(self):
        h = remove_elements([54, 23, 1, 234, 54], 54)

        assert_ll_equals_list(h, [23, 1, 234])

    def test_multiple_target_and_only_element(self):
        h = remove_elements([10, 10, 10, 10], 10)

        assert_ll_equals_list(h, [])

from typing import Optional
from core.model.listnode import ListNode
from core.testing.linked_list import assert_ll_equals_list, build_linked_list
from src.remove_duplicates_from_sorted_list.solution import Solution


def remove_duplicates(l: list) -> Optional[ListNode]:
    return Solution().deleteDuplicates(build_linked_list(l))


class TestRemoveDuplicatesFromSortedList:
    def test_empty_list(self):
        assert remove_duplicates([]) is None

    def test_list_with_one_element(self):
        h = remove_duplicates([1])

        assert_ll_equals_list(h, [1])

    def test_list_with_only_duplicate_elements(self):
        h = remove_duplicates([10, 10, 10, 10, 10])

        assert_ll_equals_list(h, [10])

    def test_list_with_no_duplicates(self):
        h = remove_duplicates([1, 2, 3, 4, 5, 6])

        assert_ll_equals_list(h, [1, 2, 3, 4, 5, 6])

    def test_list_with_multiple_duplicates(self):
        h = remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6])

        assert_ll_equals_list(h, [1, 2, 3, 4, 5, 6])

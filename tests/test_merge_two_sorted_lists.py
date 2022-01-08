from core.model.listnode import ListNode
from core.testing.linked_list import assert_ll_equals_list, build_linked_list
from src.merge_two_sorted_lists.solution import Solution


def merge_lists(arr1: list[int], arr2: list[int]):
    h1, h2 = build_linked_list(arr1), build_linked_list(arr2)

    return Solution().mergeTwoLists(h1, h2)


class TestMergeTwoSortedLists:

    def test_empty_lists(self):
        h = merge_lists([], [])

        assert h is None

    def test_first_list_empty(self):
        h = merge_lists([1, 2, 3, 4], [])

        assert_ll_equals_list(h, [1, 2, 3, 4])

    def test_second_list_empty(self):
        h = merge_lists([], [1, 2, 3, 4])

        assert_ll_equals_list(h, [1, 2, 3, 4])

    def test_first_list_shorter(self):
        h = merge_lists([1, 7, 10], [2, 3])

        assert_ll_equals_list(h, [1, 2, 3, 7, 10])

    def test_second_list_shorter(self):
        h = merge_lists([2, 3], [1, 7, 10])

        assert_ll_equals_list(h, [1, 2, 3, 7, 10])

    def test_negatives(self):
        h = merge_lists([-10, -4, -3, -1, 10], [-100, -7, 5])

        assert_ll_equals_list(h, [-100, -10, -7, -4, -3, -1, 5, 10])

    def test_no_holes_in_result(self):
        h = merge_lists([1, 3, 5, 7], [2, 4, 6, 8])

        assert_ll_equals_list(h, [1, 2, 3, 4, 5, 6, 7, 8])

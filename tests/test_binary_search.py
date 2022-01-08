from src.binary_search.solution import Solution


def search_list(nums: list[int], target: int) -> int:
    return Solution().search(nums, target)


class TestBinarySearch:

    def test_list_is_empty(self):
        assert search_list([], 10) == -1

    def test_list_len_is_1(self):
        assert search_list([10], 10) == 0

    def test_target_not_in_list(self):
        assert search_list([1, 5, 6], 3) == -1

    def test_target_is_first(self):
        assert search_list([5, 10, 23], 5) == 0

    def test_target_is_last(self):
        assert search_list([5, 10, 23], 23) == 2

    def test_target_is_mid_odd(self):
        assert search_list([5, 10, 23], 10) == 1

    def test_target_is_mid_even_first(self):
        assert search_list([5, 10, 13, 23], 10) == 1

    def test_target_is_mid_even_second(self):
        assert search_list([5, 10, 13, 23], 13) == 2

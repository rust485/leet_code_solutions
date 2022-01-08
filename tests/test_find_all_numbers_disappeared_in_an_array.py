from src.find_all_numbers_disappeared_in_an_array.solution import Solution


class TestFindAllNumbersDisappearedInAnArray:
    def test_empty_array(self):
        assert Solution().findDisappearedNumbers([]) == []

    def test_array_with_only_1(self):
        assert Solution().findDisappearedNumbers([1]) == []

    def test_array_with_two_1s(self):
        assert Solution().findDisappearedNumbers([1, 1]) == [2]

    def test_array_missing_multiple(self):
        assert Solution().findDisappearedNumbers(
            [4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

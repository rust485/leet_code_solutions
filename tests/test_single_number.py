from src.single_number.solution import Solution


class TestSingleNumber:
    def test_array_with_single_value(self):
        assert Solution().singleNumber([1]) == 1

    def test_array_missing_value_from_start(self):
        assert Solution().singleNumber([5, 1, 3, 7, 7, 1, 3]) == 5

    def test_array_missing_value_from_end(self):
        assert Solution().singleNumber([5, 1, 5, 7, 7, 1, 3]) == 3

    def test_array_missing_single_value(self):
        assert Solution().singleNumber([1, 4, 2, 1, 2]) == 4

from src.missing_number.solution import Solution


class TestMissingNumber:
    def test_empty_array(self):
        assert Solution().missingNumber([]) == 0

    def test_array_with_only_0(self):
        assert Solution().missingNumber([0]) == 1

    def test_array_with_only_1(self):
        assert Solution().missingNumber([1]) == 0

    def test_array_missing_value(self):
        assert Solution().missingNumber([5, 3, 1, 4, 7, 2, 0]) == 6

from src.convert_1d_array_into_2d_array.solution import Solution


class TestConvert1DArrayInto2DArray:
    def test_example_1(self):
        original = [1, 2, 3, 4]
        assert Solution().construct2DArray(original, 2, 2) == [[1, 2], [3, 4]]

    def test_example_2(self):
        original = [1, 2, 3]
        assert Solution().construct2DArray(original, 1, 3) == [[1, 2, 3]]

    def test_example_3(self):
        original = [1, 2]
        assert Solution().construct2DArray(original, 1, 1) == []

from src.product_of_array_except_self.solution import Solution


class TestProductOfArrayExceptSelf:
    def test_example_1(self):
        arr = [1, 2, 3, 4]
        assert Solution().productExceptSelf(arr) == [24, 12, 8, 6]

    def test_example_2(self):
        arr = [-1, 1, 0, -3, 3]
        assert Solution().productExceptSelf(arr) == [0, 0, 9, 0, 0]

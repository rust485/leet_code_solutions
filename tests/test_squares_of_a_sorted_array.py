from src.squares_of_a_sorted_array.solution import Solution

class TestSquaresOfASortedArray:
	def test_example_1(self):
		assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

	def test_example_2(self):
		assert Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
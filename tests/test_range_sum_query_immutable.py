from src.range_sum_query_immutable.solution import NumArray

class TestRangeSumQueryImmutable:

	def test_example_1(self):
		s = NumArray([-2, 0, 3, -5, 2, -1])

		assert s.sumRange(0, 2) == 1
		assert s.sumRange(2, 5) == -1
		assert s.sumRange(0, 5) == -3
		assert s.sumRange(2, 2) == 3

	def test_array_len_1(self):
		s = NumArray([5])

		assert s.sumRange(0, 0) == 5
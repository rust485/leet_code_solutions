from src.best_time_to_buy_and_sell_stock.solution import Solution

class TestBestTimeToBuyAndSellStock:

	def test_array_len_1(self):
		assert Solution().maxProfit([5]) == 0

	def test_example_1(self):
		assert Solution().maxProfit([7,1,5,3,6,4]) == 5

	def test_descending_array(self):
		assert Solution().maxProfit([7,6,4,3,1]) == 0
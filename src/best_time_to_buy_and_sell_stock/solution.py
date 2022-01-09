from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        minprice = prices[0]
        maxprofit = float('-inf')
        for i in range(1, len(prices)):
            minprice = min(minprice, prices[i])
            
            maxprofit = max(maxprofit, prices[i] - minprice)
            
        return maxprofit

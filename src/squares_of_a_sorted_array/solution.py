from heapq import heappop, heappush
from typing import List


class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		result = [0] * len(nums)

		i = r = len(nums) - 1
		l = 0

		while l <= r:
			if abs(nums[l]) > abs(nums[r]):
				result[i] = nums[l] * nums[l]
				l += 1
			else:
				result[i] = nums[r] * nums[r]
				r -= 1

			i -= 1
		
		return result
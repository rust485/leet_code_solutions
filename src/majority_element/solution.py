from typing import List
from math import ceil


class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		counts = {}

		for num in nums:
			counts[num] = 1 if num not in counts else counts[num] + 1
		
		for num in counts:
			if counts[num] > len(nums) // 2:
				return num


from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		compliments = {}
		for i in range(len(nums)):
			compliments[target - nums[i]] = i

		for i in range(len(nums)):
			if nums[i] in compliments and i != compliments[nums[i]]:
				return [i, compliments[nums[i]]]

		return []
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        sum_1_to_n = n * (n + 1) / 2

        return sum(nums) - sum_1_to_n
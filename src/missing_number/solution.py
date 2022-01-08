from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = [False] * (len(nums) + 1)

        for num in nums:
            seen[num] = True

        for i in range(len(seen)):
            if not seen[i]:
                return i

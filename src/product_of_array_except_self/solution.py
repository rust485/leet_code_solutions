from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = [1] * len(nums)

        c = 1
        for i in range(1, len(nums)):
            c *= nums[i-1]
            result[i] = c

        c = 1
        for i in reversed(range(len(nums)-1)):
            c *= nums[i+1]
            result[i] *= c

        return result

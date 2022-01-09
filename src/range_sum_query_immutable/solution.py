from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self._cache = [None] * len(nums)
        
        self._cache[0] = nums[0]
        for i in range(1,len(nums)):
            self._cache[i] = nums[i] + self._cache[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self._cache[right] - (self._cache[left-1] if left > 0 else 0)
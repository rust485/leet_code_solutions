from math import floor
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums) - 1
        l = 0

        mid = floor((h - l) / 2)
        while h >= l:
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

            mid = floor((h - l) / 2) + l

        return -1

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = [False] * len(nums)

        for n in nums:
            seen[n-1] = True

        return [i+1 for i in range(len(seen)) if not seen[i]]

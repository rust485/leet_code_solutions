from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = {}

        for n in nums:
            if n in s:
                return True
            s[n] = True

        return False

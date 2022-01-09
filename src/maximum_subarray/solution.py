from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = float('-inf')
        
        for n in nums:
            local_max = max(local_max + n, n)
            if local_max > global_max:
                global_max = local_max
                
        return global_max
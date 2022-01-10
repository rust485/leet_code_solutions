from typing import List
from math import floor

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low,high = 0,len(arr)
        
        while low < high:
            mid = floor((high - low) / 2) + low
            
            if mid > 0 and mid < len(arr) and arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            elif arr[mid] < arr[mid+1]:
                low = mid + 1
            elif arr[mid] > arr[mid+1]:
                high = mid
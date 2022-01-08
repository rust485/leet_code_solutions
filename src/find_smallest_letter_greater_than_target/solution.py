from typing import List
from math import floor


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters)-1
        idx = None
        while start <= end:
            idx = floor((end - start + 1) / 2) + start

            if letters[idx] > target:
                end = idx - 1
            else:
                start = idx + 1

        return letters[start % len(letters)]

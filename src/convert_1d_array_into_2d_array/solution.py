from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        cur_row: List[int] = []
        result: List[int] = []

        for i in range(len(original)):
            cur_row += [original[i]]

            if not ((i + 1) % n):
                result += [cur_row]
                cur_row = []

        return result

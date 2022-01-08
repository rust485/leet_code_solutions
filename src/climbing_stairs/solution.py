class Solution:
    def climbStairs(self, n: int) -> int:
        return self.rec(n, 0, {})

    def rec(self, n: int, cur: int, cache) -> int:
        if cur > n:
            return 0
        elif cur == n:
            return 1

        if cur in cache:
            return cache[cur]

        v = self.rec(n, cur + 1, cache) + self.rec(n, cur + 2, cache)
        cache[cur] = v
        return v

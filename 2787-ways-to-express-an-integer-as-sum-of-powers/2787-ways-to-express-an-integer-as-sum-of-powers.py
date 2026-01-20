class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        from functools import lru_cache
        @lru_cache(None)
        def dfs(num, target):
            if target == 0:
                return 1
            if target < 0 or num ** x > target:
                return 0
            return (dfs(num + 1, target - num ** x) + dfs(num + 1, target)) % MOD
        return dfs(1, n)
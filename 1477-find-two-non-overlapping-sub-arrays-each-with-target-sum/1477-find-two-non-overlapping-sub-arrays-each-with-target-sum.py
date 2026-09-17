class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        k = target
        A = arr
        n = len(A)
        res, total, i = n + 1, 0, 0
        dp = [n] * (n + 1)
        for j in range(n):
            total += A[j]
            while total > k:
                total -= A[i]
                i += 1
            dp[j + 1] = dp[j]
            if total == k:
                res = min(res, j - i + 1 + dp[i])
                dp[j + 1] = min(dp[j], j - i + 1)
        return -1 if res == n + 1 else res
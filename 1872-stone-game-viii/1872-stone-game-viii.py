class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        A=stones
        n = len(A)
        s = list(accumulate(A))
        @cache
        def maxDiff(i):
            if i == n - 1: return s[n - 1]
            return max(maxDiff(i + 1), s[i] - maxDiff(i + 1))
        return maxDiff(1)
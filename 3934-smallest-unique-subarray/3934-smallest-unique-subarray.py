class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        M = 1000000007
        B = 911382323
        n = len(nums)
        h = [0] * (n + 1)
        p = [1] * (n + 1)
        for i in range(n):
            h[i + 1] = (h[i] * B + nums[i]) % M
            p[i + 1] = p[i] * B % M
        def ok(k):
            c = {}
            for l in range(n - k + 1):
                r = l + k
                x = (h[r] - h[l] * p[k] % M + M) % M
                c[x] = c.get(x, 0) + 1
            return any(v == 1 for v in c.values())
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
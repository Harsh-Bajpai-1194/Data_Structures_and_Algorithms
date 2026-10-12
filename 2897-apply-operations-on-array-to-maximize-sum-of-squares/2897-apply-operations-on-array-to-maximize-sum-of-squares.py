class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        counts = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    counts[i] += 1
        ans = 0
        MOD = 10**9 + 7
        for j in range(k):
            current_num = 0
            for i in range(32):
                if counts[i] > 0:
                    current_num |= (1 << i)
                    counts[i] -= 1
            ans = (ans + current_num * current_num) % MOD
        return ans
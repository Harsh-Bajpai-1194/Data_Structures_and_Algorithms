class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        difference = [0] * (2*limit + 2)
        for i in range(n // 2):
            a = min(nums[i], nums[n-i-1])
            b = max(nums[i], nums[n-i-1])
            difference[2] += 2
            difference[a + 1] -= 1
            difference[a + b] -= 1
            difference[a + b + 1] += 1
            difference[b + limit + 1] += 1
        minimum, current = n, 0
        for c in range(2, 2*limit + 1):
            current += difference[c]
            minimum=min(current,minimum)
        return minimum
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum=max(nums)
        c=0
        n=len(nums)
        for i in range(n):
            c+=maximum-nums[i]
        return c
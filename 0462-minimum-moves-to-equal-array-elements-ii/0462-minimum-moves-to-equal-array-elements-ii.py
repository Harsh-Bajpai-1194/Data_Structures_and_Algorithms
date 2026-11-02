class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median=nums[len(nums)//2]
        c=0
        for i in nums:
            c+=abs(i-median)
        return c
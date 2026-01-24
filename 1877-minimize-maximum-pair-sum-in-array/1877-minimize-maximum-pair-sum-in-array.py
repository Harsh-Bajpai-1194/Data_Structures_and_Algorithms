class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum=0
        for i in range(len(nums)//2): sum=max(sum,nums[i]+nums[len(nums)-i-1])
        return sum
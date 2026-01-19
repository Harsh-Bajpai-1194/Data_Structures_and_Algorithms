class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]
        L=nums[:]
        for i in range(len(nums)-1):
            L[i]=(nums[i]+nums[i+1])%10
        L.pop(-1)
        return self.triangularSum(L)
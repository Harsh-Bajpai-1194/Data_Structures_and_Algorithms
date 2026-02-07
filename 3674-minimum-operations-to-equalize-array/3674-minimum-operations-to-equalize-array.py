class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums
        if len(set(a))==1: return 0
        nums.sort()
        s=nums[0]
        for i in range(1,len(nums)):
            s=s&nums[i]
        return 1
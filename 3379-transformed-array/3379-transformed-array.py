class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[0]*len(nums)
        for i in range(len(nums)): 
            L[i]=nums[(i+nums[i])%len(nums)]
        return L
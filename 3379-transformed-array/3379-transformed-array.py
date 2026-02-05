class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        L=[0]*n
        for i in range(n): 
            L[i]=nums[(i+nums[i])%n]
        return L
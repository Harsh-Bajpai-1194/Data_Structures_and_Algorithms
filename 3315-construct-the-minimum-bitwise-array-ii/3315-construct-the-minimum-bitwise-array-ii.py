class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            ans,d=-1,1
            while (nums[i]&d)!=0: ans,d=nums[i]-d,d<<1
            nums[i]=ans
        return nums
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[0]*len(nums)
        for i in range(len(nums)):
            for k in range(len(nums)):
                if nums[i]>nums[k]: L[i]+=1
        return L
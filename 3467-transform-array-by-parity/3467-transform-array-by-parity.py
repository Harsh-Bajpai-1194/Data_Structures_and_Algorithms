class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i]%2==0: nums[i]=0
            else: nums[i]=1
        nums.sort()
        return nums
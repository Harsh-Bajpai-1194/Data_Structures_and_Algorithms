class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            if nums[i]<k: c+=1
        return c
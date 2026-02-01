class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=0
        c=0
        for i in range(len(nums)):
            if nums[i]==1: c+=1; maximum=max(c,maximum)
            else: c=0
        return maximum
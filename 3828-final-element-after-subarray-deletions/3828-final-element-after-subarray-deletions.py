class Solution(object):
    def finalElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=len(nums)
        if a==1: return nums[0]
        else:
            b=nums
            return max(nums[0],nums[-1])
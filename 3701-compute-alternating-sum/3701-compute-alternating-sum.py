class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]
        else:
            for i in range(1,len(nums),2):
                nums[i]*=-1
        return sum(nums)
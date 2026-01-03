class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        nums.sort()
        for i in range(0,len(nums),2): sum+=min(nums[i],nums[i+1])
        return sum
class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2: return -1
        nums.remove(max(nums))
        nums.remove(min(nums))
        return nums[0]
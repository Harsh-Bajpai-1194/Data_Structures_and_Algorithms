class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L=nums[:]
        nums.sort()
        if nums[-1]>=nums[-2]*2: return L.index(nums[-1])
        return -1
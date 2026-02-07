class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums: c+=max(nums)-i
        return c
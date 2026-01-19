class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        S=set(nums)
        while original in S: original*=2
        return original
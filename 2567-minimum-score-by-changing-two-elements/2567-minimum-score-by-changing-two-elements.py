class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = nsmallest(3, nums)
        large = nlargest(3, nums)
        return min(large[0] - small[2], large[1] - small[1], large[2] - small[0])
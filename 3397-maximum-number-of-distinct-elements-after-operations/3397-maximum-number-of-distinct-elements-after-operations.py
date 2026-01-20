class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        last = -float('inf')
        res = 0
        for x in nums:
            candidate = max(x - k, last + 1)
            if candidate <= x + k:
                res += 1
                last = candidate
        return res
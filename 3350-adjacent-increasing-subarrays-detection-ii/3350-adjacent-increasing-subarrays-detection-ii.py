class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        inc_end = [1] * n
        inc_start = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_end[i] = inc_end[i-1] + 1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                inc_start[i] = inc_start[i+1] + 1
        res = 0
        for i in range(n-1):
            res = max(res, min(inc_end[i], inc_start[i+1]))
        return res
class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = abs(nums[0] - nums[-1])
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i - 1])
            if diff > ans:
                ans = diff
        return ans
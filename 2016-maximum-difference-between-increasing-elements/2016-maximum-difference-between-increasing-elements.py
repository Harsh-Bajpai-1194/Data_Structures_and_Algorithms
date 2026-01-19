class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        max_diff = -1
        for x in nums[1:]:
            if x > min_val:
                diff = x - min_val
                if diff > max_diff:
                    max_diff = diff
            else:
                min_val = x
        return max_diff
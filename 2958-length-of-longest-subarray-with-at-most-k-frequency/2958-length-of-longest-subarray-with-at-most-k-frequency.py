class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = {}
        i = c = 0
        for j in range(len(nums)):
            m[nums[j]] = m.get(nums[j], 0) + 1
            while m[nums[j]] > k:
                m[nums[i]] -= 1
                i += 1
            c = max(c, j - i + 1)
        return c
class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def is_increasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        n = len(nums)
        for i in range(n - 2*k + 1):
            if is_increasing(i) and is_increasing(i + k):
                return True
        return False
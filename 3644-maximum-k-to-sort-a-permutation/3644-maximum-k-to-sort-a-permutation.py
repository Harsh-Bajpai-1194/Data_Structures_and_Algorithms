class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = -1
        for i in range(n):
            if nums[i] == i:
                continue
            a = a&nums[i]
        return 0 if a == -1 else a
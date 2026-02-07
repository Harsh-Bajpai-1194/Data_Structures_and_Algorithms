class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        if k>=len(nums): return 0
        else: return abs(sum(nums[-1:-k-1:-1])-sum(nums[0:k]))
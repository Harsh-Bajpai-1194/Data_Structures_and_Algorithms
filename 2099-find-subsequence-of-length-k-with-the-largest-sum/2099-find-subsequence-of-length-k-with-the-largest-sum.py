class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """  
        n = len(nums)  
        indices = sorted(range(n), key=lambda i: nums[i], reverse=True)[:k]  
        indices.sort()  
        return [nums[i] for i in indices]  
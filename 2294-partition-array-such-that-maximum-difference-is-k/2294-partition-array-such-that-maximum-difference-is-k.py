class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 1
        start = nums[0]
        for num in nums:
            if num - start > k:
                count += 1
                start = num
        return count
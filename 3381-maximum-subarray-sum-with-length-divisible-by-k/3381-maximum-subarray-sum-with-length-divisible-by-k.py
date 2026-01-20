class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        max_sum = -float('inf')
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = (i + 1) % k
            if min_prefix[remainder] != float('inf'):
                current_valid_sum = prefix_sum - min_prefix[remainder]
                if current_valid_sum > max_sum: max_sum = current_valid_sum
            if prefix_sum < min_prefix[remainder]: min_prefix[remainder] = prefix_sum
        return max_sum if max_sum != -float('inf') else 0
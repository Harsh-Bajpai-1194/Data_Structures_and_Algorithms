class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        max_length = 0
        for i in range(len(nums)):
            curr_length = 1
            for pos in range(i + 1, len(nums)):
                if nums[pos] > nums[pos - 1]: curr_length += 1
                else: break
            max_length = max(max_length, curr_length)
        for i in range(len(nums)):
            curr_length = 1
            for pos in range(i + 1, len(nums)):
                if nums[pos] < nums[pos - 1]: curr_length += 1
                else: break
            max_length = max(max_length, curr_length)
        return max_length
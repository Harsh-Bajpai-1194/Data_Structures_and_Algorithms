class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = float("-inf")
        i = 0
        while i < n:
            j = i + 1
            res = 0
            while j < n and nums[j - 1] < nums[j]:
                j += 1
            p = j - 1
            if p == i:
                i += 1
                continue
            res += nums[p] + nums[p - 1]
            while j < n and nums[j - 1] > nums[j]:
                res += nums[j]
                j += 1
            q = j - 1
            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q
                continue
            res += nums[q + 1]
            max_sum = 0
            curr_sum = 0
            k = q + 2
            while k < n and nums[k] > nums[k - 1]:
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
                k += 1
            res += max_sum
            max_sum = 0
            curr_sum = 0
            for k in range(p - 2, i - 1, -1):
                curr_sum += nums[k]
                max_sum = max(max_sum, curr_sum)
            res += max_sum
            ans = max(ans, res)
            i = q
        return ans
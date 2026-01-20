class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        def can(x):
            cnt = i = 0
            while i + 1 < len(nums) and cnt < p:
                if nums[i+1] - nums[i] <= x:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
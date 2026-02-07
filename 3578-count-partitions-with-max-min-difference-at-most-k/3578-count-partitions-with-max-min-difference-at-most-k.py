class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque
        n = len(nums)
        MOD = 10**9 + 7
        p = [0] * (n + 2)
        p[1] = 1
        min_q = deque()
        max_q = deque()
        l = 0
        for r in range(n):
            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()
            min_q.append(r)
            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()
            max_q.append(r)
            while nums[max_q[0]] - nums[min_q[0]] > k:
                l += 1
                if min_q[0] < l:
                    min_q.popleft()
                if max_q[0] < l:
                    max_q.popleft()
            curr = (p[r + 1] - p[l]) % MOD
            p[r + 2] = (p[r + 1] + curr) % MOD
        return (p[n + 1] - p[n]) % MOD
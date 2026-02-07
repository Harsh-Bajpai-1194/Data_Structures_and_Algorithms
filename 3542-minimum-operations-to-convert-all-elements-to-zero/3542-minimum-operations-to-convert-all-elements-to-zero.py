class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pse = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)  
        total_ops = 0
        last_pos = {}
        for i, val in enumerate(nums):
            if val == 0:
                continue
            if val not in last_pos or pse[i] > last_pos[val]:
                total_ops += 1
            last_pos[val] = i
        return total_ops
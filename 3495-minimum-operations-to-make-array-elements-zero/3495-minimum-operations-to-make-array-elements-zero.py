class Solution(object):
    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        def steps_sum(l, r):
            total = 0
            k = 1
            base = 1
            while base <= r:
                left = max(l, base)
                right = min(r, base*4 - 1)
                if left <= right:
                    count = right - left + 1
                    total += count * k
                base *= 4
                k += 1
            return total
        ans = 0
        for l, r in queries:
            total_steps = steps_sum(l, r)
            ans += (total_steps + 1) // 2 
        return ans
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        n = len(nums) // 3    
        left_sum = [0] * (2 * n + 1)  
        heap = []  
        current_sum = 0  
        for i in range(n):  
            heapq.heappush(heap, -nums[i])  
            current_sum += nums[i]  
        left_sum[n] = current_sum  
        for i in range(n, 2 * n):  
            current_sum += nums[i] + heapq.heappushpop(heap, -nums[i])  
            left_sum[i+1] = current_sum    
        right_sum = [0] * (2 * n + 1)  
        heap = []  
        current_sum = 0  
        for i in range(3 * n - 1, 2 * n - 1, -1):  
            heapq.heappush(heap, nums[i])  
            current_sum += nums[i]  
        right_sum[2*n] = current_sum  
        for i in range(2 * n - 1, n - 1, -1):  
            current_sum += nums[i] - heapq.heappushpop(heap, nums[i])  
            right_sum[i] = current_sum  
        min_diff = float('inf')  
        for i in range(n, 2 * n + 1):  
            min_diff = min(min_diff, left_sum[i] - right_sum[i])  
        return min_diff
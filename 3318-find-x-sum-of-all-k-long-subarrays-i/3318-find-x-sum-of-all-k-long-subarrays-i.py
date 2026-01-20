class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        from collections import Counter
        n = len(nums)
        answer = []
        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            counts = Counter(subarray)
            if len(counts) < x:
                answer.append(sum(subarray))
                continue            
            sorted_elements = sorted(counts.items(), 
                                     key=lambda item: (item[1], item[0]), 
                                     reverse=True)
            top_x_values = set(item[0] for item in sorted_elements[:x])
            current_x_sum = 0
            for num in subarray:
                if num in top_x_values: current_x_sum += num
            answer.append(current_x_sum)
        return answer
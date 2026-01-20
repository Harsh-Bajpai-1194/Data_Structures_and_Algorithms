class Solution:
    def minOperations(self, nums: List[int]) -> int:
        import math 
        n = len(nums)
        ones = nums.count(1)
        if ones > 0: return n - ones
        minOps = float('inf')
        for i, g in enumerate(nums):
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])  
                if g == 1:
                    minOps = min(minOps, j - i)
                    break          
        return -1 if minOps == float('inf') else minOps + n - 1
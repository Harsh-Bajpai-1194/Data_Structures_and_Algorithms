class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  
        left, right = 0, len(nums) - 1  
        result = 0  
        mod = 10**9 + 7  
        powers = [1] * len(nums)  
        for i in range(1, len(nums)):  
            powers[i] = (powers[i - 1] * 2) % mod  
        while left <= right:  
            if nums[left] + nums[right] <= target:  
                result = (result + powers[right - left]) % mod  
                left += 1  
            else:  
                right -= 1  
        return result